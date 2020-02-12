from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class Login(FlaskForm):
    email = EmailField('Email', validators=[DataRequired])
    password = PasswordField('Password', validators=[DataRequired])
    remember = BooleanField('Remember Me')
