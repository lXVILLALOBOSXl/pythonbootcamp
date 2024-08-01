from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    TextAreaField,
    BooleanField,
    SelectField,
)
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional, Regexp


choices = [
    ("AGU", "Aguascalientes"),
    ("BCN", "Baja California Norte"),
    ("BCS", "Baja California Sur"),
    ("CAM", "Campeche"),
    ("CHP", "Chiapas"),
    ("CHH", "Chihuahua"),
    ("COA", "Coahuila"),
    ("COL", "Colima"),
    ("CDMX", "Ciudad de México"),
    ("DUR", "Durango"),
    ("GUA", "Guanajuato"),
    ("GRO", "Guerrero"),
    ("HID", "Hidalgo"),
    ("JAL", "Jalisco"),
    ("MEX", "México"),
    ("MIC", "Michoacán"),
    ("MOR", "Morelos"),
    ("NAY", "Nayarit"),
    ("NLE", "Nuevo León"),
    ("OAX", "Oaxaca"),
    ("PUE", "Puebla"),
    ("QUE", "Querétaro"),
    ("ROO", "Quintana Roo"),
    ("SLP", "San Luis Potosí"),
    ("SIN", "Sinaloa"),
    ("SON", "Sonora"),
    ("TAB", "Tabasco"),
    ("TAM", "Tamaulipas"),
    ("TLA", "Tlaxcala"),
    ("VER", "Veracruz"),
    ("YUC", "Yucatán"),
    ("ZAC", "Zacatecas"),
]


class NotifyExistencesForm(FlaskForm):
    name = StringField("Nombre *", validators=[DataRequired()])
    email = StringField("Email *", validators=[DataRequired(), Email()])
    comments = TextAreaField("Comentarios")
    submit = SubmitField("Notificarme", render_kw={"class": "btn btn-primary"})

    def __init__(self, name=None, email=None, *args, **kwargs):
        super(NotifyExistencesForm, self).__init__(*args, **kwargs)
        if name:
            self.name.data = name
        if email:
            self.email.data = email


class LoginForm(FlaskForm):
    email = StringField("Correo Electrónico", validators=[DataRequired(), Email()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField(
        "Iniciar sesión", render_kw={"class": "btn btn-primary btn-block"}
    )


class RegisterForm(FlaskForm):
    name = StringField("Nombre *", validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField("Correo Electrónico *", validators=[DataRequired(), Email()])
    phone = StringField("Celular *", validators=[DataRequired(), Length(min=10, max=10)], render_kw={"pattern": "[0-9]{10}", "title": "Verifica el número celular"})
    password = PasswordField("Contraseña *", validators=[DataRequired(), Length(min=8)], render_kw={"pattern": "^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!.?-])[A-Za-z\d@$!.?-]{8,}$", "title": "La contraseña debe contener al menos una mayúscula, una minúscula, un número y un caracter especial"})
    confirm_password = PasswordField(
        "Confirmar Contraseña *", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField(
        "Crear cuenta", render_kw={"class": "btn btn-success btn-block"}
    )


class RequestResetForm(FlaskForm):
    email = StringField("Correo Electrónico", validators=[DataRequired(), Email()])
    submit = SubmitField(
        "Restablecer", render_kw={"class": "btn btn-primary btn-block"}
    )


class ResetPasswordForm(FlaskForm):
    password = PasswordField(
        "Nueva Contraseña", validators=[DataRequired(), Length(min=8)], render_kw={"pattern": "^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!.?-])[A-Za-z\d@$!.?-]{8,}$", "title": "La contraseña debe contener al menos una mayúscula, una minúscula, un número y un caracter especial"}
    )
    confirm_password = PasswordField(
        "Confirmar Nueva Contraseña", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField(
        "Restablecer Contraseña", render_kw={"class": "btn btn-primary btn-block"}
    )


class CheckoutForm(FlaskForm):
    shipping_nombre = StringField(
        "Nombre *", validators=[Optional(), Length(min=1, max=100)]
    )
    shipping_apellidos = StringField(
        "Apellidos *", validators=[Optional(), Length(min=1, max=100)]
    )
    shipping_celular = StringField(
        "Celular *", validators=[Optional(), Length(min=10, max=10)], render_kw={"pattern": "[0-9]{10}", "title": "Verifica el número celular"}
    )
    shipping_empresa = StringField(
        "Empresa", validators=[Optional(), Length(max=100)], default=""
    )
    shipping_calle = StringField(
        "Calle *", validators=[Optional(), Length(min=1, max=100)]
    )
    shipping_numero = StringField(
        "Número *", validators=[Optional(), Length(min=1, max=10)],
        render_kw={"pattern": "^\d{1,10}$", "title": "Verifica el Número"}
    )
    shipping_num_int = StringField(
        "Número Interior", validators=[Optional(), Length(max=10)], default=""
    )
    shipping_referencias = StringField(
        "Referencias", validators=[Optional(), Length(max=255)], default=""
    )
    shipping_colonia = StringField(
        "Colonia *", validators=[Optional(), Length(min=1, max=100)]
    )
    shipping_cp = StringField(
        "Código Postal *", validators=[Optional(), Length(min=5, max=5)], render_kw={"pattern": "^\\d{5}$", "title": "Verifica el código postal"}
    )
    shipping_ciudad = StringField(
        "Ciudad *", validators=[Optional(), Length(min=1, max=100)]
    )
    shipping_estado = SelectField("Estado *", validators=[Optional()], choices=choices)

    same_address = BooleanField(
        "La dirección de facturación coincide con la dirección de envío", default=True
    )
    payment_nombre = StringField(
        "Nombre *", validators=[Optional(), Length(min=1, max=100)]
    )
    payment_apellidos = StringField(
        "Apellidos *", validators=[Optional(), Length(min=1, max=100)]
    )
    payment_calle = StringField(
        "Calle *", validators=[Optional(), Length(min=1, max=100)]
    )
    payment_numero = StringField(
        "Número *", validators=[Optional(), Length(min=1, max=10)],
        render_kw={"pattern": "^\d{1,10}$", "title": "Verifica el Número"}
    )
    payment_num_int = StringField(
        "Número Interior", validators=[Optional(), Length(max=10)], default=""
    )
    payment_referencias = StringField(
        "Referencias", validators=[Optional(), Length(max=255)], default=""
    )
    payment_colonia = StringField(
        "Colonia *", validators=[Optional(), Length(min=1, max=100)]
    )
    payment_cp = StringField(
        "Código Postal *", validators=[Optional(), Length(min=5, max=5)], render_kw={"pattern": "^\\d{5}$", "title": "Verifica el código postal"}
    )
    payment_ciudad = StringField(
        "Ciudad *", validators=[Optional(), Length(min=1, max=100)]
    )
    payment_estado = SelectField("Estado *", validators=[Optional()], choices=choices)

    need_invoice = BooleanField("Necesito Factura")
    payment_rfc = StringField(
        "RFC *", validators=[Optional(), Length(max=13)], default=""
    )
    payment_razon_social = StringField(
        "Razón Social o nombre *", validators=[Optional(), Length(max=100)], default=""
    )
    cp_invoice = StringField(
        "Código Postal *", validators=[Optional(), Length(min=5, max=5)], default="", render_kw={"pattern": "^\\d{5}$", "title": "Verifica el código postal"}
    )
    payment_regimen_fiscal = SelectField(
        "Régimen Fiscal *",
        validators=[Optional()],
        choices=[("R1", "Régimen 1"), ("R2", "Régimen 2")],
        default="",
    )
    uso_cfdi = SelectField(
        "Uso CFDI *",
        validators=[Optional()],
        choices=[("U1", "Uso 1"), ("U2", "Uso 2")],
        default="",
    )

    submit = SubmitField("Completar Compra")


class ShippingAddressForm(FlaskForm):
    nombre = StringField("Nombre *", validators=[DataRequired(), Length(min=1, max=100)])
    apellidos = StringField(
        "Apellidos *", validators=[DataRequired(), Length(min=1, max=100)]
    )
    celular = StringField("Celular *", validators=[DataRequired(), Length(min=10, max=10)],render_kw={"pattern": "[0-9]{10}", "title": "Verifica el número celular"})
    empresa = StringField(
        "Empresa", validators=[Optional(), Length(max=100)], default=""
    )
    calle = StringField("Calle *", validators=[DataRequired(), Length(min=1, max=100)])
    numero = StringField("Número *", validators=[DataRequired(), Length(min=1, max=10)], render_kw={"pattern": "^\d{1,10}$", "title": "Verifica el Número"})
    num_int = StringField(
        "Número Interior", validators=[Optional(), Length(max=10)], default=""
    )
    referencias = StringField(
        "Referencias", validators=[Optional(), Length(max=255)], default=""
    )
    colonia = StringField("Colonia *", validators=[DataRequired(), Length(min=1, max=100)])
    cp = StringField("Código Postal *", validators=[DataRequired(), Length(min=5, max=5)], render_kw={"pattern": "^\\d{5}$", "title": "Verifica el código postal"})
    ciudad = StringField("Ciudad *", validators=[DataRequired(), Length(min=1, max=100)])
    estado = SelectField("Estado *", validators=[DataRequired()], choices=choices)
    submit = SubmitField("Guardar Dirección de Envío")


class PaymentAddressForm(FlaskForm):
    nombre = StringField("Nombre *", validators=[DataRequired(), Length(min=1, max=100)])
    apellidos = StringField(
        "Apellidos *", validators=[DataRequired(), Length(min=1, max=100)]
    )
    calle = StringField("Calle *", validators=[DataRequired(), Length(min=1, max=100)])
    numero = StringField("Número *", validators=[DataRequired(), Length(min=1, max=10)], render_kw={"pattern": "^\d{1,10}$", "title": "Verifica el Número"})
    num_int = StringField(
        "Número Interior", validators=[Optional(), Length(max=10)], default=""
    )
    referencias = StringField(
        "Referencias", validators=[Optional(), Length(max=255)], default=""
    )
    colonia = StringField("Colonia *", validators=[DataRequired(), Length(min=1, max=100)])
    cp = StringField("Código Postal *", validators=[DataRequired(), Length(min=5, max=5)], render_kw={"pattern": "^\\d{5}$", "title": "Verifica el código postal"})
    ciudad = StringField("Ciudad *", validators=[DataRequired(), Length(min=1, max=100)])
    estado = SelectField("Estado *", validators=[DataRequired()], choices=choices)
    submit = SubmitField("Guardar Dirección de Facturación")


class BillingForm(FlaskForm):
    rfc = StringField("RFC *", validators=[DataRequired(), Length(max=13)], default="")
    razon_social = StringField(
        "Razón Social o nombre *", validators=[DataRequired(), Length(max=100)], default=""
    )
    cp = StringField(
        "Código Postal *", validators=[DataRequired(), Length(min=5, max=5)], default="", render_kw={"pattern": "^\\d{5}$", "title": "Verifica el código postal"}
    )
    regimen_fiscal = SelectField(
        "Régimen Fiscal *",
        validators=[DataRequired()],
        choices=[("R1", "Régimen 1"), ("R2", "Régimen 2")],
        default="",
    )
    uso_cfdi = SelectField(
        "Uso CFDI *",
        validators=[DataRequired()],
        choices=[("U1", "Uso 1"), ("U2", "Uso 2")],
        default="",
    )
    submit = SubmitField("Guardar Información de Facturación")

class AccountConfigForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Correo Electrónico', validators=[DataRequired(), Email()])
    phone = StringField('Celular', validators=[DataRequired(), Length(min=10, max=10)],render_kw={"pattern": "[0-9]{10}", "title": "Verifica el número celular"}) 
    actual_password = PasswordField('Contraseña actual', validators=[DataRequired()])
    password = PasswordField('Nueva Contraseña', validators=[Optional(), Length(min=8)], render_kw={"pattern": "^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!.?-])[A-Za-z\d@$!.?-]{8,}$", "title": "La contraseña debe contener al menos una mayúscula, una minúscula, un número y un caracter especial"})
    confirm_password = PasswordField('Confirmar Contraseña', validators=[
        Optional(),
        EqualTo('password')
    ])
    submit = SubmitField('Actualizar') 