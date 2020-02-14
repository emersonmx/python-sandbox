from flask import render_template


def dashboard():
    return 'Dashboard'


def login():
    from .forms import Login
    form = Login()
    return render_template('login.html', form=form)


def logout():
    return 'Logout'
