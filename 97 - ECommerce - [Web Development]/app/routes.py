from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from .models import Product, Client, ShippingAddress, PaymentAddress, Order, OrderItem, ProductImage
from .forms import *
main = Blueprint('main', __name__)

@main.route('/')
def index():
    featured_products = Product.query.filter_by(is_featured=True).order_by(Product.date_added.desc()).limit(9).all()
    new_products = Product.query.order_by(Product.date_added.desc()).limit(9).all()
    offer_products = Product.query.filter(Product.old_price > Product.price).order_by(Product.date_added.desc()).limit(9).all()
    return render_template('index.html', products=featured_products, new_products=new_products, offers=offer_products)

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
            'stock': product.units_in_stock
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

@main.route('/checkout')
def checkout():
    # Aquí puedes añadir la lógica para el pago
    return render_template('checkout.html')





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
    
    

@main.route('/login')
def login():
    pass

@main.route('/register')
def register():
    pass

@main.route('/search')
def search():
    pass

