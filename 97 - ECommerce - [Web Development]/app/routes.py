from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from .models import (
    Product,
    Client,
    ShippingAddress,
    PaymentAddress,
    Order,
    OrderItem,
    ProductImage,
    Billing,
)
from .forms import *
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from . import db
from .utils import (
    send_confirmation_email,
    send_reset_email,
    confirm_token,
    send_guest_confirmation_email,
)
from sqlalchemy.orm import joinedload
import datetime


main = Blueprint("main", __name__)


@main.route("/")
def index():
    featured_products = (
        Product.query.filter_by(is_featured=True)
        .order_by(Product.date_added.desc())
        .limit(9)
        .all()
    )
    new_products = Product.query.order_by(Product.date_added.desc()).limit(9).all()
    offer_products = (
        Product.query.filter(Product.old_price > Product.price)
        .order_by(Product.date_added.desc())
        .limit(9)
        .all()
    )
    return render_template(
        "index.html",
        products=featured_products,
        new_products=new_products,
        offers=offer_products,
    )


@main.route("/notify/<int:id>", methods=["GET", "POST"])
def notify(id):
    form = NotifyExistencesForm()
    product = Product.query.get_or_404(id)
    if form.validate_on_submit():
        flash(
            "Será notificado cuando el producto se encuentre en existencia", "success"
        )
        # Send email to admin with the form data
        print(f"Name: {form.name.data}")
        print(f"Email: {form.email.data}")
        print(f"Comments: {form.comments.data}")
        print(f"Product: {product.name}")
        return redirect(url_for("main.index"))
    return render_template("notify.html", form=form)


@main.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        next_page = request.args.get("next")
        return redirect(next_page or url_for("main.index"))

    form = LoginForm()
    next_page = request.args.get("next")

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = Client.query.filter_by(email=email).first()

        if not user:
            flash(
                "Correo o contraseña incorrecta, por favor intenta de nuevo.", "danger"
            )
            return redirect(url_for("main.login", next=next_page))
        elif not check_password_hash(user.password_hash, password):
            flash(
                "Correo o contraseña incorrecta, por favor intenta de nuevo.", "danger"
            )
            return redirect(url_for("main.login", next=next_page))
        else:
            login_user(user)
            return redirect(
                next_page or url_for("main.index")
            )  # Redirect to the next page if available, otherwise to the index page

    return render_template(
        "login.html", logged_in=current_user.is_authenticated, form=form
    )


@main.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = RegisterForm()
    next_page = request.args.get("next")

    if form.validate_on_submit():
        email = form.email.data
        user = Client.query.filter_by(email=email).first()
        if user:
            flash(
                "Ese correo electrónico ya está registrado. Por favor, inicia sesión.",
                "danger",
            )
            return redirect(url_for("main.login", next=next_page))

        hash_and_salted_password = generate_password_hash(
            form.password.data, method="pbkdf2:sha256", salt_length=8
        )
        new_user = Client(
            email=form.email.data,
            password_hash=hash_and_salted_password,
            name=form.name.data,
            is_verified=False,
        )
        db.session.add(new_user)
        db.session.commit()

        send_confirmation_email(new_user.email)

        flash(
            "Se ha enviado un correo electrónico de confirmación por email.", "success"
        )
        return redirect(url_for("main.login", next=next_page))

    return render_template(
        "register.html",
        logged_in=current_user.is_authenticated,
        form=form,
        next=next_page,
    )


@main.route("/control-panel")
@login_required
def control_panel():
    user = current_user
    return render_template("control_panel.html", user=user)


@main.route("/orders")
@login_required
def orders():
    user = current_user
    orders = (
        Order.query.filter_by(client_id=user.id)
        .order_by(Order.date_ordered.desc())
        .options(joinedload(Order.order_items).joinedload(OrderItem.product))
        .all()
    )
    return render_template("orders.html", orders=orders)


@main.route("/account", methods=["GET", "POST"])
@login_required
def account():
    user = current_user
    form = AccountConfigForm(obj=current_user)

    if form.validate_on_submit():
        if check_password_hash(user.password_hash, form.password.data):
            user.name = form.name.data
            if user.email != form.email.data:
                user.email = form.email.data
                user.is_verified = False
            user.phone = form.phone.data
            if form.new_password.data:
                user.password_hash = generate_password_hash(
                    form.new_password.data, method="pbkdf2:sha256", salt_length=8
                )
            db.session.commit()
            flash("Tu cuenta ha sido actualizada", "success")
            return redirect(url_for("main.account"))
        else:
            flash("Contraseña incorrecta", "danger")
            return redirect(url_for("main.account"))

    return render_template("account.html", form=form, is_verified=user.is_verified)


@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@main.route("/send_verification_email", methods=["GET", "POST"])
@login_required
def send_verification_email():
    if current_user.is_verified:
        flash("Tu cuenta ya está verificada.", "success")
        return redirect(url_for("main.account"))
    send_confirmation_email(current_user.email)

    flash(
        "Se ha enviado un correo de verificación a tu dirección de correo electrónico.",
        "success",
    )

    return redirect(url_for("main.account"))


@main.route("/checkout", methods=["GET", "POST"])
def checkout():
    cart = session.get("cart", [])

    if not cart:
        return redirect(url_for("main.index"))

    if not current_user.is_authenticated:
        flash(
            "Por favor inicia sesión o crea una cuenta para proceder con la compra.",
            "warning",
        )
        return redirect(url_for("main.checkout_options", next=url_for("main.checkout")))

    if not current_user.is_verified:
        send_confirmation_email(current_user.email)
        flash(
            "Tu cuenta no está verificada. Se ha enviado un correo electrónico de verificación. Por favor, verifica tu correo electrónico para proceder con la compra.",
            "warning",
        )
        return redirect(url_for("main.cart"))

    saved_shipping_addresses = ShippingAddress.query.filter_by(
        client_id=current_user.id, is_deleted=False
    ).all()
    saved_payment_addresses = PaymentAddress.query.filter_by(
        client_id=current_user.id, is_deleted=False
    ).all()
    saved_billing_info = Billing.query.filter_by(
        client_id=current_user.id, is_deleted=False
    ).all()

    form = CheckoutForm()
    total = sum(item["price"] * item["quantity"] for item in cart)

    if form.validate_on_submit():
        shipping_address_id = request.form.get("shipping_address")
        payment_address_id = request.form.get("payment_address")
        billing_info_id = request.form.get("billing_info")

        if shipping_address_id == "new":
            shipping_address = ShippingAddress(
                client_id=current_user.id,
                nombre=form.shipping_nombre.data,
                apellidos=form.shipping_apellidos.data,
                celular=form.shipping_celular.data,
                empresa=form.shipping_empresa.data,
                calle=form.shipping_calle.data,
                numero=form.shipping_numero.data,
                num_int=form.shipping_num_int.data,
                referencias=form.shipping_referencias.data,
                colonia=form.shipping_colonia.data,
                cp=form.shipping_cp.data,
                ciudad=form.shipping_ciudad.data,
                estado=form.shipping_estado.data,
            )
            db.session.add(shipping_address)
            db.session.flush()
        else:
            shipping_address = ShippingAddress.query.get(shipping_address_id)

        if form.same_address.data:
            # If the shipping address is already saved in payment address, don't save it again
            existing_payment_address = PaymentAddress.query.filter_by(
                client_id=current_user.id,
                nombre=shipping_address.nombre,
                apellidos=shipping_address.apellidos,
                calle=shipping_address.calle,
                numero=shipping_address.numero,
                num_int=shipping_address.num_int,
                referencias=shipping_address.referencias,
                colonia=shipping_address.colonia,
                cp=shipping_address.cp,
                ciudad=shipping_address.ciudad,
                estado=shipping_address.estado,
            ).first()
            if existing_payment_address:
                payment_address = existing_payment_address
            else:
                payment_address = PaymentAddress(
                    client_id=current_user.id,
                    nombre=shipping_address.nombre,
                    apellidos=shipping_address.apellidos,
                    calle=shipping_address.calle,
                    numero=shipping_address.numero,
                    num_int=shipping_address.num_int,
                    referencias=shipping_address.referencias,
                    colonia=shipping_address.colonia,
                    cp=shipping_address.cp,
                    ciudad=shipping_address.ciudad,
                    estado=shipping_address.estado,
                )
                db.session.add(payment_address)
                db.session.flush()
        elif payment_address_id == "new":
            payment_address = PaymentAddress(
                client_id=current_user.id,
                nombre=form.payment_nombre.data,
                apellidos=form.payment_apellidos.data,
                calle=form.payment_calle.data,
                numero=form.payment_numero.data,
                num_int=form.payment_num_int.data,
                referencias=form.payment_referencias.data,
                colonia=form.payment_colonia.data,
                cp=form.payment_cp.data,
                ciudad=form.payment_ciudad.data,
                estado=form.payment_estado.data,
            )
            db.session.add(payment_address)
            db.session.flush()
        else:
            payment_address = PaymentAddress.query.get(payment_address_id)

        if form.need_invoice.data:
            if billing_info_id == "new":
                billing_info = Billing(
                    client_id=current_user.id,
                    rfc=form.payment_rfc.data,
                    razon_social=form.payment_razon_social.data,
                    regimen_fiscal=form.payment_regimen_fiscal.data,
                    uso_cfdi=form.uso_cfdi.data,
                    cp=form.cp_invoice.data,
                )
                db.session.add(billing_info)
                db.session.flush()
            else:
                billing_info = Billing.query.get(billing_info_id)
        else:
            billing_info = None

        order = Order(
            client_id=current_user.id,
            total_amount=total,
            billing_id=billing_info.id if billing_info else None,
            shipping_address_id=shipping_address.id,
            payment_address_id=payment_address.id,
            forma_de_pago="",
            metodo_de_pago="",
        )
        db.session.add(order)
        db.session.flush()

        for item in cart:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item["id"],
                quantity=item["quantity"],
                price=item["price"],
            )
            db.session.add(order_item)
            # update stock
            product = Product.query.get(item["id"])
            product.units_in_stock -= item["quantity"]
            db.session.add(product)

        # Clear the cart
        session["cart"] = []

        db.session.commit()
        flash("Compra completada con éxito.", "success")
        return redirect(url_for("main.index"))
    elif request.method == "POST":
        flash("Por favor completa los campos necesarios *", "danger")

    return render_template(
        "checkout_form.html",
        form=form,
        cart=cart,
        total=total,
        saved_shipping_addresses=saved_shipping_addresses,
        saved_payment_addresses=saved_payment_addresses,
        saved_billing_info=saved_billing_info,
    )


@main.route("/addresses", methods=["GET", "POST"])
@login_required
def addresses():
    saved_addresses = ShippingAddress.query.filter_by(
        client_id=current_user.id, is_deleted=False
    ).all()

    form = ShippingAddressForm()

    if form.validate_on_submit():
        new_address = ShippingAddress(
            client_id=current_user.id,
            nombre=form.nombre.data,
            apellidos=form.apellidos.data,
            celular=form.celular.data,
            empresa=form.empresa.data,
            calle=form.calle.data,
            numero=form.numero.data,
            num_int=form.num_int.data,
            referencias=form.referencias.data,
            colonia=form.colonia.data,
            cp=form.cp.data,
            ciudad=form.ciudad.data,
            estado=form.estado.data,
        )
        db.session.add(new_address)
        db.session.commit()
        flash("Dirección de envío agregada con éxito", "success")
        return redirect(url_for("main.addresses"))

    return render_template("addresses.html", form=form, saved_addresses=saved_addresses)


@main.route("/edit_address/<int:id>", methods=["GET", "POST"])
def edit_address(id):
    if not current_user.is_authenticated:
        return redirect(url_for("main.index"))
    address = ShippingAddress.query.get_or_404(id)
    if address.client_id != current_user.id:
        return redirect(url_for("main.index"))

    form = ShippingAddressForm(obj=address)
    if form.validate_on_submit():
        existing_address = ShippingAddress.query.filter_by(
            client_id=current_user.id,
            nombre=form.nombre.data,
            apellidos=form.apellidos.data,
            calle=form.calle.data,
            numero=form.numero.data,
            num_int=form.num_int.data,
            referencias=form.referencias.data,
            colonia=form.colonia.data,
            cp=form.cp.data,
            ciudad=form.ciudad.data,
            estado=form.estado.data,
        ).first()
        if existing_address:
            address.is_deleted = True
            existing_address.is_deleted = False
        else:
            shipping_address = ShippingAddress(
                client_id=current_user.id,
                nombre=form.nombre.data,
                apellidos=form.apellidos.data,
                celular=form.celular.data,
                empresa=form.empresa.data,
                calle=form.calle.data,
                numero=form.numero.data,
                num_int=form.num_int.data,
                referencias=form.referencias.data,
                colonia=form.colonia.data,
                cp=form.cp.data,
                ciudad=form.ciudad.data,
                estado=form.estado.data,
            )
            address.is_deleted = True
            db.session.add(shipping_address)
        db.session.commit()
        flash("Dirección editada exitosamente.", "success")
        next_page = request.args.get("next")
        if not next_page:
            next_page = url_for("main.account")
        return redirect(next_page)
    return render_template("edit_address.html", form=form)


@main.route("/payment-addresses", methods=["GET", "POST"])
@login_required
def payment_addresses():
    saved_addresses = PaymentAddress.query.filter_by(
        client_id=current_user.id, is_deleted=False
    ).all()

    form = PaymentAddressForm()

    if form.validate_on_submit():
        new_address = PaymentAddress(
            client_id=current_user.id,
            nombre=form.nombre.data,
            apellidos=form.apellidos.data,
            calle=form.calle.data,
            numero=form.numero.data,
            num_int=form.num_int.data,
            referencias=form.referencias.data,
            colonia=form.colonia.data,
            cp=form.cp.data,
            ciudad=form.ciudad.data,
            estado=form.estado.data,
        )
        db.session.add(new_address)
        db.session.commit()
        flash("Dirección de facturación agregada con éxito", "success")
        return redirect(url_for("main.payment_addresses"))

    return render_template(
        "payment_addresses.html", form=form, saved_addresses=saved_addresses
    )


@main.route("/edit_payment/<int:id>", methods=["GET", "POST"])
def edit_payment(id):
    if not current_user.is_authenticated:
        return redirect(url_for("main.index"))
    address = PaymentAddress.query.get_or_404(id)
    if address.client_id != current_user.id:
        return redirect(url_for("main.index"))

    form = PaymentAddressForm(obj=address)
    if form.validate_on_submit():
        existing_address = PaymentAddress.query.filter_by(
            client_id=current_user.id,
            nombre=form.nombre.data,
            apellidos=form.apellidos.data,
            calle=form.calle.data,
            numero=form.numero.data,
            num_int=form.num_int.data,
            referencias=form.referencias.data,
            colonia=form.colonia.data,
            cp=form.cp.data,
            ciudad=form.ciudad.data,
            estado=form.estado.data,
        ).first()
        if existing_address:
            address.is_deleted = True
            existing_address.is_deleted = False
        else:
            payment_address = PaymentAddress(
                client_id=current_user.id,
                nombre=form.nombre.data,
                apellidos=form.apellidos.data,
                calle=form.calle.data,
                numero=form.numero.data,
                num_int=form.num_int.data,
                referencias=form.referencias.data,
                colonia=form.colonia.data,
                cp=form.cp.data,
                ciudad=form.ciudad.data,
                estado=form.estado.data,
            )
            address.is_deleted = True
            db.session.add(payment_address)
        db.session.commit()
        flash("Dirección editada exitosamente.", "success")
        next_page = request.args.get("next")
        if not next_page:
            next_page = url_for("main.account")
        return redirect(next_page)
    return render_template("edit_payment.html", form=form)


@main.route("/billing-info", methods=["GET", "POST"])
@login_required
def billing_info():
    saved_billing_info = Billing.query.filter_by(
        client_id=current_user.id, is_deleted=False
    ).all()

    form = BillingForm()

    if form.validate_on_submit():
        new_billing_info = Billing(
            client_id=current_user.id,
            rfc=form.rfc.data,
            razon_social=form.razon_social.data,
            cp=form.cp.data,
            regimen_fiscal=form.regimen_fiscal.data,
            uso_cfdi=form.uso_cfdi.data,
        )
        db.session.add(new_billing_info)
        db.session.commit()
        flash("Información de facturación agregada con éxito", "success")
        return redirect(url_for("main.billing_info"))

    return render_template(
        "billing_info.html", form=form, saved_billing_info=saved_billing_info
    )


@main.route("/edit_billing/<int:id>", methods=["GET", "POST"])
def edit_billing(id):
    if not current_user.is_authenticated:
        return redirect(url_for("main.index"))
    address = Billing.query.get_or_404(id)
    if address.client_id != current_user.id:
        return redirect(url_for("main.index"))

    form = BillingForm(obj=address)
    if form.validate_on_submit():
        existing_address = Billing.query.filter_by(
            client_id=current_user.id,
            rfc=form.rfc.data,
            razon_social=form.razon_social.data,
            regimen_fiscal=form.regimen_fiscal.data,
            uso_cfdi=form.uso_cfdi.data,
            cp=form.cp.data,
        ).first()
        if existing_address:
            address.is_deleted = True
            existing_address.is_deleted = False
        else:
            billing_info = Billing(
                client_id=current_user.id,
                rfc=form.rfc.data,
                razon_social=form.razon_social.data,
                regimen_fiscal=form.regimen_fiscal.data,
                uso_cfdi=form.uso_cfdi.data,
                cp=form.cp.data,
            )
            address.is_deleted = True
            db.session.add(billing_info)
        db.session.commit()
        flash("Información de facturación editada exitosamente.", "success")
        next_page = request.args.get("next")
        if not next_page:
            next_page = url_for("main.account")
        return redirect(next_page)
    return render_template("edit_billing.html", form=form)


@main.route("/delete_address/<int:id>", methods=["GET", "POST"])
def delete_address(id):
    if not current_user.is_authenticated:
        return redirect(url_for("main.index"))
    address = ShippingAddress.query.get_or_404(id)
    if address.client_id != current_user.id:
        return redirect(url_for("main.index"))

    # Marcar la dirección como eliminada
    address.is_deleted = True
    db.session.add(address)
    db.session.commit()

    flash("Dirección eliminada exitosamente.", "success")

    next_page = request.args.get("next")
    if not next_page:
        next_page = url_for("main.account")

    return redirect(next_page)


@main.route("/delete_payment/<int:id>", methods=["GET", "POST"])
def delete_payment(id):
    if not current_user.is_authenticated:
        return redirect(url_for("main.index"))
    address = PaymentAddress.query.get_or_404(id)
    if address.client_id != current_user.id:
        return redirect(url_for("main.index"))

    # Marcar la dirección como eliminada
    address.is_deleted = True
    db.session.add(address)
    db.session.commit()

    flash("Dirección eliminada exitosamente.", "success")

    next_page = request.args.get("next")
    if not next_page:
        next_page = url_for("main.account")

    return redirect(next_page)


@main.route("/delete_billing/<int:id>", methods=["GET", "POST"])
def delete_billing(id):
    if not current_user.is_authenticated:
        return redirect(url_for("main.index"))
    address = Billing.query.get_or_404(id)
    if address.client_id != current_user.id:
        return redirect(url_for("main.index"))

    # Marcar la dirección como eliminada
    address.is_deleted = True
    db.session.add(address)
    db.session.commit()

    flash("Información de facturación eliminada exitosamente.", "success")

    next_page = request.args.get("next")
    if not next_page:
        next_page = url_for("main.account")

    return redirect(next_page)


@main.route("/checkout_options")
def checkout_options():
    next_page = request.args.get("next")
    return render_template("checkout_options.html", next=next_page)


@main.route("/confirm/<token>")
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash("El enlace de confirmación no es válido o ha caducado.", "danger")
        return redirect(url_for("main.login"))

    user = Client.query.filter_by(email=email).first_or_404()
    if user.is_verified:
        flash("Cuenta ya confirmada. Por favor Iniciar sesión.", "success")
    else:
        user.is_verified = True
        db.session.add(user)
        db.session.commit()
        flash("Has confirmado tu cuenta. ¡Gracias!", "success")
    return redirect(url_for("main.login"))


@main.route("/reset", methods=["GET", "POST"])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = Client.query.filter_by(email=form.email.data).first()
        if user:
            send_reset_email(user.email)
            flash(
                "Se ha enviado un correo electrónico con instrucciones para restablecer su contraseña.",
                "success",
            )
            return redirect(url_for("main.login"))
    return render_template("reset_request.html", form=form)


@main.route("/reset/<token>", methods=["GET", "POST"])
def reset_with_token(token):
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    email = confirm_token(token)
    if not email:
        flash("El enlace de reinicio no es válido o ha caducado.", "danger")
        return redirect(url_for("main.reset_request"))

    user = Client.query.filter_by(email=email).first_or_404()

    # Check if the token is already used or expired
    if (
        user.reset_token != token
        or user.reset_token_expiration < datetime.datetime.utcnow()
    ):
        flash("El enlace de reinicio no es válido o ha caducado.", "danger")
        return redirect(url_for("main.reset_request"))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.password_hash = generate_password_hash(
            form.password.data, method="pbkdf2:sha256", salt_length=8
        )
        user.reset_token = None  # Invalidate the token
        user.reset_token_expiration = None  # Remove expiration
        db.session.commit()
        flash("¡Tu contraseña ha sido actualizada!", "success")
        return redirect(url_for("main.login"))

    return render_template("reset_token.html", form=form, token=token)


@main.route("/product/<int:id>")
def product(id):
    product = Product.query.get_or_404(id)
    images = product.images
    return render_template("product.html", product=product, images=images)


@main.route("/add/<int:id>", methods=["POST"])
def add(id):
    product = Product.query.get_or_404(id)
    selected_quantity = int(
        request.form.get("quantity", 1)
    )  # Get the selected quantity from the form, default to 1

    if "cart" not in session:
        session["cart"] = []

    cart = session["cart"]

    for item in cart:
        if item["id"] == product.id:
            item["quantity"] = min(
                item["quantity"] + selected_quantity, item["stock"]
            )  # Ensure not to exceed stock
            break
    else:
        cart.append(
            {
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "quantity": selected_quantity,
                "stock": product.units_in_stock,
                "old_price": product.old_price,
            }
        )

    session["cart"] = cart
    flash(
        f"{selected_quantity} unidad(es) de {product.name} añadido(s) a tu carrito!",
        "success",
    )

    return redirect(url_for("main.index"))


@main.route("/remove/<int:id>", methods=["POST"])
def remove(id):
    if "cart" in session:
        cart = session["cart"]
        session["cart"] = [item for item in cart if item["id"] != id]
        flash("Artículo eliminado del carrito", "success")
    return redirect(url_for("main.cart"))


@main.route("/update/<int:id>", methods=["POST"])
def update(id):
    quantity = int(request.form.get("quantity"))
    if "cart" in session:
        cart = session["cart"]
        for item in cart:
            if item["id"] == id:
                item["quantity"] = min(
                    quantity, item["stock"]
                )  # Ensure quantity does not exceed stock
                break
        session["cart"] = cart
        flash("Carrito actualizado", "success")
    return redirect(url_for("main.cart"))


@main.route("/cart")
def cart():
    cart = session.get("cart", [])
    total = sum(item["price"] * item["quantity"] for item in cart)
    return render_template("cart.html", cart=cart, total=total)


@main.route("/search")
def search():
    pass
