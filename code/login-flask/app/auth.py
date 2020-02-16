from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from app.models import User
from app.forms import Login


def dashboard():
    return render_template('dashboard.html')


def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'), current_user=current_user)

    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('dashboard'))

    return render_template('login.html', form=form)


def logout():
    logout_user()
    return redirect(url_for('dashboard'))
