from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired

class ResponseForm(FlaskForm):
    respuesta = IntegerField('respuesta', validators=[DataRequired()])