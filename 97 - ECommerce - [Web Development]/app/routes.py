from flask import Blueprint, render_template, redirect, url_for, flash
from .models import Product, Client, ShippingAddress, PaymentAddress, Order, OrderItem

main = Blueprint('main', __name__)

@main.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products, new_products=products, offers=products)

@main.route('/login')
def login():
    pass

@main.route('/register')
def register():
    pass

@main.route('/search')
def search():
    pass

