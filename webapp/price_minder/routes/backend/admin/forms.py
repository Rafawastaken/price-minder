from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

class ApiForm(FlaskForm):
    key = StringField('Password', validators=[DataRequired()])
