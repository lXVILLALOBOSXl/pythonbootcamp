from datetime import datetime
from . import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  
    internal_sku = db.Column(db.String(50), unique=True, nullable=False)
    brand_sku = db.Column(db.String(50))
    price = db.Column(db.Float, nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    units = db.Column(db.String(10), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    units_in_stock = db.Column(db.Integer, nullable=False)
    img_src = db.Column(db.String(255), nullable=True) 

    def __repr__(self):
        return f'<Product {self.internal_sku}>'
    

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    shipping_addresses = db.relationship('ShippingAddress', backref='client', lazy=True)
    payment_addresses = db.relationship('PaymentAddress', backref='client', lazy=True)
    orders = db.relationship('Order', backref='client', lazy=True)

    def __repr__(self):
        return f'<Client {self.name}>'

class ShippingAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    calle = db.Column(db.String(100), nullable=False)
    colonia = db.Column(db.String(100), nullable=False)
    municipio = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    referencias = db.Column(db.String(255))
    entre_calle_1 = db.Column(db.String(100))
    entre_calle_2 = db.Column(db.String(100))
    num_int = db.Column(db.String(10))
    
    def __repr__(self):
        return f'<ShippingAddress {self.nombre}>'

class PaymentAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    calle = db.Column(db.String(100), nullable=False)
    colonia = db.Column(db.String(100), nullable=False)
    municipio = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    referencias = db.Column(db.String(255))
    entre_calle_1 = db.Column(db.String(100))
    entre_calle_2 = db.Column(db.String(100))
    num_int = db.Column(db.String(10))
    
    def __repr__(self):
        return f'<PaymentAddress {self.nombre}>'

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    date_ordered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total_amount = db.Column(db.Float, nullable=False)
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
