from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional

class NotifyExistencesForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    comments = TextAreaField('Comentarios (opcional)')
    submit = SubmitField('Notificarme', render_kw={"class": "btn btn-primary"})

class LoginForm(FlaskForm):
    email = StringField('Correo Electrónico', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión', render_kw={"class": "btn btn-primary btn-block"})

class RegisterForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Correo Electrónico', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Crear cuenta', render_kw={"class": "btn btn-success btn-block"})

class RequestResetForm(FlaskForm):
    email = StringField('Correo Electrónico', validators=[DataRequired(), Email()])
    submit = SubmitField('Restablecer', render_kw={"class": "btn btn-primary btn-block"})

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Nueva Contraseña', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmar Nueva Contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Restablecer Contraseña', render_kw={"class": "btn btn-primary btn-block"})


class CheckoutForm(FlaskForm):
    shipping_nombre = StringField('Nombre *', validators=[Optional(), Length(min=1, max=100)])
    shipping_apellidos = StringField('Apellidos *', validators=[Optional(), Length(min=1, max=100)])
    shipping_celular = StringField('Celular *', validators=[Optional(), Length(min=10, max=10)])
    shipping_empresa = StringField('Empresa', validators=[Optional(), Length(max=100)], default="")
    shipping_calle = StringField('Calle *', validators=[Optional(), Length(min=1, max=100)])
    shipping_numero = StringField('Número *', validators=[Optional(), Length(min=1, max=10)])
    shipping_num_int = StringField('Número Interior', validators=[Optional(), Length(max=10)], default="")
    shipping_referencias = StringField('Referencias', validators=[Optional(), Length(max=255)], default="")
    shipping_colonia = StringField('Colonia *', validators=[Optional(), Length(min=1, max=100)])
    shipping_cp = StringField('Código Postal *', validators=[Optional(), Length(min=5, max=5)])
    shipping_ciudad = StringField('Ciudad *', validators=[Optional(), Length(min=1, max=100)])
    shipping_estado = SelectField('Estado *', validators=[Optional()],
                                 choices=[
                                     ('AGU', 'Aguascalientes'),
                                     ('BCN', 'Baja California Norte'),
                                     ('BCS', 'Baja California Sur'),
                                     ('CAM', 'Campeche'),
                                     ('CHP', 'Chiapas'),
                                     ('CHH', 'Chihuahua'),
                                     ('COA', 'Coahuila'),
                                     ('COL', 'Colima'),
                                     ('CDMX', 'Ciudad de México'),
                                     ('DUR', 'Durango'),
                                     ('GUA', 'Guanajuato'),
                                     ('GRO', 'Guerrero'),
                                     ('HID', 'Hidalgo'),
                                     ('JAL', 'Jalisco'),
                                     ('MEX', 'México'),
                                     ('MIC', 'Michoacán'),
                                     ('MOR', 'Morelos'),
                                     ('NAY', 'Nayarit'),
                                     ('NLE', 'Nuevo León'),
                                     ('OAX', 'Oaxaca'),
                                     ('PUE', 'Puebla'),
                                     ('QUE', 'Querétaro'),
                                     ('ROO', 'Quintana Roo'),
                                     ('SLP', 'San Luis Potosí'),
                                     ('SIN', 'Sinaloa'),
                                     ('SON', 'Sonora'),
                                     ('TAB', 'Tabasco'),
                                     ('TAM', 'Tamaulipas'),
                                     ('TLA', 'Tlaxcala'),
                                     ('VER', 'Veracruz'),
                                     ('YUC', 'Yucatán'),
                                     ('ZAC', 'Zacatecas')
                                 ])
    save_shipping = BooleanField('Guardar para futuras compras')

    same_address = BooleanField('La dirección de facturación coincide con la dirección de envío', default=True)
    payment_nombre = StringField('Nombre *', validators=[Optional(), Length(min=1, max=100)])
    payment_apellidos = StringField('Apellidos *', validators=[Optional(), Length(min=1, max=100)])
    payment_calle = StringField('Calle *', validators=[Optional(), Length(min=1, max=100)])
    payment_numero = StringField('Número *', validators=[Optional(), Length(min=1, max=10)])
    payment_num_int = StringField('Número Interior', validators=[Optional(), Length(max=10)], default="")
    payment_referencias = StringField('Referencias', validators=[Optional(), Length(max=255)], default="")
    payment_colonia = StringField('Colonia *', validators=[Optional(), Length(min=1, max=100)])
    payment_cp = StringField('Código Postal *', validators=[Optional(), Length(min=5, max=5)])
    payment_ciudad = StringField('Ciudad *', validators=[Optional(), Length(min=1, max=100)])
    payment_estado = SelectField('Estado *', validators=[Optional()],
                                 choices=[
                                     ('AGU', 'Aguascalientes'),
                                     ('BCN', 'Baja California Norte'),
                                     ('BCS', 'Baja California Sur'),
                                     ('CAM', 'Campeche'),
                                     ('CHP', 'Chiapas'),
                                     ('CHH', 'Chihuahua'),
                                     ('COA', 'Coahuila'),
                                     ('COL', 'Colima'),
                                     ('CDMX', 'Ciudad de México'),
                                     ('DUR', 'Durango'),
                                     ('GUA', 'Guanajuato'),
                                     ('GRO', 'Guerrero'),
                                     ('HID', 'Hidalgo'),
                                     ('JAL', 'Jalisco'),
                                     ('MEX', 'México'),
                                     ('MIC', 'Michoacán'),
                                     ('MOR', 'Morelos'),
                                     ('NAY', 'Nayarit'),
                                     ('NLE', 'Nuevo León'),
                                     ('OAX', 'Oaxaca'),
                                     ('PUE', 'Puebla'),
                                     ('QUE', 'Querétaro'),
                                     ('ROO', 'Quintana Roo'),
                                     ('SLP', 'San Luis Potosí'),
                                     ('SIN', 'Sinaloa'),
                                     ('SON', 'Sonora'),
                                     ('TAB', 'Tabasco'),
                                     ('TAM', 'Tamaulipas'),
                                     ('TLA', 'Tlaxcala'),
                                     ('VER', 'Veracruz'),
                                     ('YUC', 'Yucatán'),
                                     ('ZAC', 'Zacatecas')
                                 ])
    save_payment = BooleanField('Guardar para futuras compras')

    need_invoice = BooleanField('Necesito Factura')
    payment_rfc = StringField('RFC *', validators=[Optional(), Length(max=13)], default="")
    payment_razon_social = StringField('Razón Social o nombre *', validators=[Optional(), Length(max=100)], default="")
    cp_invoice = StringField('Código Postal *', validators=[Optional(), Length(min=5, max=5)], default="")
    payment_regimen_fiscal = SelectField('Régimen Fiscal *', validators=[Optional()], choices=[('R1', 'Régimen 1'), ('R2', 'Régimen 2')], default="")
    uso_cfdi = SelectField('Uso CFDI *',validators=[Optional()], choices=[('U1', 'Uso 1'), ('U2', 'Uso 2')], default="")
    save_billing = BooleanField('Guardar para futuras compras')

    submit = SubmitField('Completar Compra')
