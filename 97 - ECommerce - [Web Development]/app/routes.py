from flask import Blueprint, render_template, redirect, url_for, flash
from .models import Product, Client, ShippingAddress, PaymentAddress, Order, OrderItem
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
    return render_template('product.html', product=product)

@main.route('/add/<int:id>')
def add(id):
    product = Product.query.get_or_404(id)
    return render_template('add.html', product=product)

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

