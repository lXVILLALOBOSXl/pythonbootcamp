from datetime import datetime
from sqlalchemy import text, ForeignKeyConstraint
from . import db, login_manager
from flask_login import UserMixin

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  
    internal_sku = db.Column(db.String(50), unique=True, nullable=False)
    brand_sku = db.Column(db.String(50), default='N/A', server_default='N/A')
    price = db.Column(db.Float, nullable=False)
    brand = db.Column(db.String(50), default='N/A', server_default='N/A')
    description = db.Column(db.Text, default='N/A', server_default='N/A') 
    units = db.Column(db.String(10), default='N/A', server_default='N/A')
    category = db.Column(db.String(50), default='N/A', server_default='N/A')
    units_in_stock = db.Column(db.Integer, default=0, server_default='0')
    old_price = db.Column(db.Float, nullable=True)
    is_featured = db.Column(db.Boolean, default=False, server_default='0')
    date_added = db.Column(db.DateTime, default=datetime.now, server_default=text("CURRENT_TIMESTAMP"))
    img_src = db.Column(db.String(255), nullable=True)
    images = db.relationship('ProductImage', backref='product', lazy=True)

    def __repr__(self):
        return f'<Product {self.internal_sku}>'

class ProductImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    img_src = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<ProductImage {self.img_src}>'

class Client(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_verified = db.Column(db.Boolean, default=False, server_default='0')
    shipping_addresses = db.relationship('ShippingAddress', backref='client', lazy=True)
    payment_addresses = db.relationship('PaymentAddress', backref='client', lazy=True)
    billing = db.relationship('Billing', backref='client', lazy=True)
    orders = db.relationship('Order', backref='client', lazy=True)
    reset_token = db.Column(db.String(120), nullable=True)
    reset_token_expiration = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Client {self.name}>'

@login_manager.user_loader
def load_user(user_id):
    return Client.query.get(int(user_id))

class Billing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    rfc = db.Column(db.String(13), nullable=False)
    razon_social = db.Column(db.String(100), nullable=False)
    regimen_fiscal = db.Column(db.String(100), nullable=False)
    uso_cfdi = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Billing {self.rfc}>'

class ShippingAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    celular = db.Column(db.String(10), nullable=False)
    empresa = db.Column(db.String(100))
    calle = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    num_int = db.Column(db.String(10))
    referencias = db.Column(db.String(255))
    colonia = db.Column(db.String(100), nullable=False)
    cp = db.Column(db.String(5), nullable=False)
    ciudad = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<ShippingAddress {self.nombre}>'
    
class PaymentAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    calle = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    num_int = db.Column(db.String(10))
    referencias = db.Column(db.String(255))
    colonia = db.Column(db.String(100), nullable=False)
    cp = db.Column(db.String(5), nullable=False)
    ciudad = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(100), nullable=False)
    rfc = db.Column(db.String(13), nullable=True)
    razon_social = db.Column(db.String(100), nullable=True)
    regimen_fiscal = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<PaymentAddress {self.nombre}>'

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    date_ordered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total_amount = db.Column(db.Float, nullable=False)
    uso_cfdi = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(50), nullable=False, default='Pending')
    shipping_address_id = db.Column(db.Integer, db.ForeignKey('shipping_address.id'), nullable=False)
    payment_address_id = db.Column(db.Integer, db.ForeignKey('payment_address.id'), nullable=False)
    shipping_address = db.relationship('ShippingAddress', backref='orders')
    payment_address = db.relationship('PaymentAddress', backref='orders')
    order_items = db.relationship('OrderItem', backref='order', lazy=True)

    def __repr__(self):
        return f'<Order {self.id}>'

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<OrderItem {self.id}>'
