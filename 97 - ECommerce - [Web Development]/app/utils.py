from itsdangerous import URLSafeTimedSerializer
from flask import current_app, url_for, render_template
from flask_mail import Message
from . import mail
from .models import Client
import datetime
from . import db

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=current_app.config['SECURITY_PASSWORD_SALT'])

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=current_app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except Exception:
        return False
    return email

def send_reset_email(user_email):
    user = Client.query.filter_by(email=user_email).first()
    if user:
        token = generate_confirmation_token(user_email)
        user.reset_token = token
        user.reset_token_expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        db.session.commit()
        
        reset_url = url_for('main.reset_with_token', token=token, _external=True)
        html = render_template('reset_password_email.html', reset_url=reset_url)
        send_email(user_email, 'Reset Your Password', html)

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=current_app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)

def send_confirmation_email(user_email):
    token = generate_confirmation_token(user_email)
    confirm_url = url_for('main.confirm_email', token=token, _external=True)
    html = render_template('confirm.html', confirm_url=confirm_url)
    send_email(user_email, 'Confirme su email', html)

def send_guest_confirmation_email(order):
    token = generate_confirmation_token(order.email)
    confirm_url = url_for('main.confirm_order_email', token=token, _external=True)
    html = render_template('confirm_order.html', confirm_url=confirm_url, order=order)
    send_email(order.email, 'Confirm Your Order', html)

