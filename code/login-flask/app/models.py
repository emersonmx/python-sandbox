from sqlalchemy_mixins import AllFeaturesMixin

from app import db
from app import sqlalchemy as sa


class Base(db.Model, AllFeaturesMixin):
    __abstract__ = True


class User(Base, sa.Timestamp):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
