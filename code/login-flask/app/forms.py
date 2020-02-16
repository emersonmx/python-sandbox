from flask_wtf import FlaskForm
from wtforms.fields import PasswordField
from wtforms.fields.html5 import EmailField


class Login(FlaskForm):
    email = EmailField('Email')
    password = PasswordField('Password')
