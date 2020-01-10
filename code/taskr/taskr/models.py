from sqlalchemy.ext.hybrid import hybrid_property
from flask_security import UserMixin
from sqlalchemy_mixins import AllFeaturesMixin

from taskr import db
from taskr.sqlalchemy import mixins


class Base(db.Model, AllFeaturesMixin):
    __abstract__ = True


class BoardUser(Base):
    __tablename__ = 'board_user'

    name = db.Column(db.String(255), nullable=False)
    permission = db.Column(db.String(255), nullable=False)
    board_id = db.Column(
        db.Integer(), db.ForeignKey('boards.id'), primary_key=True
    )
    user_id = db.Column(
        db.Integer(), db.ForeignKey('users.id'), primary_key=True
    )

    board = db.relationship('Board', back_populates='users')
    user = db.relationship('User', back_populates='boards')


class User(Base, UserMixin, mixins.Timestamp):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

    boards = db.relationship('BoardUser', back_populates='user')

    @hybrid_property
    def roles(self):
        return []

    @roles.setter
    def roles(self, role):
        pass


class Board(Base, mixins.Timestamp, mixins.SoftDelete):
    __tablename__ = 'boards'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    users = db.relationship('BoardUser', back_populates='board')
