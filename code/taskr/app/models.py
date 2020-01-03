from sqlalchemy_mixins import AllFeaturesMixin

from app import db
from app import mixins


class User(db.Model, AllFeaturesMixin, mixins.Timestamp):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
