from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class NotifyExistencesForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    comments = TextAreaField('Comentarios (opcional)')
    submit = SubmitField('Notificarme', render_kw={"class": "btn btn-primary"})



