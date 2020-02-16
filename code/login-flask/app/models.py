from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_mixins import AllFeaturesMixin
from flask_login import UserMixin

from app import db, login
from app import sqlalchemy as sa


class Base(db.Model, AllFeaturesMixin):
    __abstract__ = True


Base.set_session(db.session)


class User(Base, sa.Timestamp, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
