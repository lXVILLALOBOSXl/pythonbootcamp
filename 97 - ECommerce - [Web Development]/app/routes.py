from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from .models import Product, Client, ShippingAddress, PaymentAddress, Order, OrderItem, ProductImage
from .forms import *
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from . import db
from .utils import send_confirmation_email, send_reset_email, confirm_token, send_guest_confirmation_email

main = Blueprint('main', __name__)

@main.route('/')
def index():
    featured_products = Product.query.filter_by(is_featured=True).order_by(Product.date_added.desc()).limit(9).all()
    new_products = Product.query.order_by(Product.date_added.desc()).limit(9).all()
    offer_products = Product.query.filter(Product.old_price > Product.price).order_by(Product.date_added.desc()).limit(9).all()
    return render_template('index.html', products=featured_products, new_products=new_products, offers=offer_products)

@main.route('/notify/<int:id>', methods=['GET', 'POST'])
def notify(id):
    form = NotifyExistencesForm()
    product = Product.query.get_or_404(id)
    if form.validate_on_submit():
        flash('Será notificado cuando el producto se encuentre en existencia', 'success')
        # Send email to admin with the form data
        print(f'Name: {form.name.data}')
        print(f'Email: {form.email.data}')
        print(f'Comments: {form.comments.data}')
        print(f'Product: {product.name}')
        return redirect(url_for('main.index'))
    return render_template('notify.html', form=form)
    
@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = Client.query.filter_by(email=email).first()
        if not user:
            flash('Correo o contraseña incorrecta, por favor intenta de nuevo.', 'error')
            return redirect(url_for('main.login'))
        elif not check_password_hash(user.password_hash, password):
            flash('Correo o contraseña incorrecta, por favor intenta de nuevo.', 'error')
            return redirect(url_for('main.login'))
        elif not user.is_verified:
            send_confirmation_email(user.email)
            flash('Tu cuenta no está verificada. Se ha enviado un correo electrónico de verificación. Por favor, verifica tu correo electrónico para iniciar sesión.', 'warning')
            return redirect(url_for('main.login'))
        else:
            login_user(user)
            return redirect(url_for('main.index'))  # Redirect to the desired page after login
    return render_template("login.html", logged_in=current_user.is_authenticated, form=form)


@main.route('/confirm_order/<token>')
def confirm_order_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
        return redirect(url_for('main.index'))

    order = Order.query.filter_by(email=email).first_or_404()
    if order.is_confirmed:
        flash('Order already confirmed.', 'success')
    else:
        order.is_confirmed = True
        db.session.add(order)
        db.session.commit()
        flash('Your order has been confirmed. Thanks!', 'success')
    return redirect(url_for('main.index'))


@main.route('/account')
@login_required
def account():
    user = current_user
    shipping_addresses = ShippingAddress.query.filter_by(client_id=user.id).all()
    payment_addresses = PaymentAddress.query.filter_by(client_id=user.id).all()
    orders = Order.query.filter_by(client_id=user.id).all()
    return render_template('account.html', user=user, shipping_addresses=shipping_addresses, payment_addresses=payment_addresses, orders=orders)


@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    if not current_user.is_verified:
        send_confirmation_email(current_user.email)
        flash('Tu cuenta no está verificada. Se ha enviado un correo electrónico de verificación. Por favor, verifica tu correo electrónico para proceder con la compra.', 'warning')
        return redirect(url_for('main.cart'))
    
    form = CheckoutForm()
    if form.validate_on_submit():
        # Handle form submission, save addresses, and create order here
        # ...

        flash('Compra completada con éxito.', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('checkout_form.html', form=form)




@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        user = Client.query.filter_by(email=email).first()
        if user:
            flash("Ese correo electrónico ya está registrado. Por favor, inicia sesión.", 'danger')
            return redirect(url_for('main.login'))
        
        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = Client(
            email=form.email.data,
            password_hash=hash_and_salted_password,
            name=form.name.data,
            is_verified=False
        )
        db.session.add(new_user)
        db.session.commit()

        send_confirmation_email(new_user.email)

        flash('Se ha enviado un correo electrónico de confirmación por email.', 'success')
        return redirect(url_for('main.login'))
    
    return render_template('register.html', logged_in=current_user.is_authenticated, form=form)

@main.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('El enlace de confirmación no es válido o ha caducado.', 'danger')
        return redirect(url_for('main.login'))

    user = Client.query.filter_by(email=email).first_or_404()
    if user.is_verified:
        flash('Cuenta ya confirmada. Por favor Iniciar sesión.', 'success')
    else:
        user.is_verified = True
        db.session.add(user)
        db.session.commit()
        flash('Has confirmado tu cuenta. ¡Gracias!', 'success')
    return redirect(url_for('main.login'))

@main.route('/reset', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = Client.query.filter_by(email=form.email.data).first()
        if user:
            send_reset_email(user.email)
            flash('Se ha enviado un correo electrónico con instrucciones para restablecer su contraseña.', 'success')
            return redirect(url_for('main.login'))
    return render_template('reset_request.html', form=form)

@main.route('/reset/<token>', methods=['GET', 'POST'])
def reset_with_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    try:
        email = confirm_token(token)
    except:
        flash('El enlace de reinicio no es válido o ha caducado.', 'danger')
        return redirect(url_for('main.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user = Client.query.filter_by(email=email).first_or_404()
        user.password_hash = generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=8)
        db.session.add(user)
        db.session.commit()
        flash('¡Tu contraseña ha sido actualizada!', 'success')
        return redirect(url_for('main.login'))
    return render_template('reset_token.html', form=form, token=token)


@main.route('/product/<int:id>')
def product(id):
    product = Product.query.get_or_404(id)
    images = product.images
    return render_template('product.html', product=product, images=images)


@main.route('/add/<int:id>', methods=['POST'])
def add(id):
    product = Product.query.get_or_404(id)

    if 'cart' not in session:
        session['cart'] = []

    cart = session['cart']

    for item in cart:
        if item['id'] == product.id:
            item['quantity'] = min(item['quantity'] + 1, item['stock'])  # Ensure not to exceed stock
            break
    else:
        cart.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'quantity': 1,
            'stock': product.units_in_stock,
            'old_price': product.old_price
        })

    session['cart'] = cart
    flash(f'Producto {product.name} añandido a tu carrito!', 'success')
    
    return redirect(url_for('main.index'))

@main.route('/remove/<int:id>', methods=['POST'])
def remove(id):
    if 'cart' in session:
        cart = session['cart']
        session['cart'] = [item for item in cart if item['id'] != id]
        flash('Artículo eliminado del carrito', 'success')
    return redirect(url_for('main.cart'))

@main.route('/update/<int:id>', methods=['POST'])
def update(id):
    quantity = int(request.form.get('quantity'))
    if 'cart' in session:
        cart = session['cart']
        for item in cart:
            if item['id'] == id:
                item['quantity'] = min(quantity, item['stock'])  # Ensure quantity does not exceed stock
                break
        session['cart'] = cart
        flash('Carrito actualizado', 'success')
    return redirect(url_for('main.cart'))

@main.route('/cart')
def cart():
    cart = session.get('cart', [])
    total = sum(item['price'] * item['quantity'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)





@main.route('/search')
def search():
    pass

