from flask_security import UserMixin, RoleMixin
from sqlalchemy_mixins import AllFeaturesMixin

from app import db
from app import mixins


class Base(db.Model, AllFeaturesMixin):
    __abstract__ = True


class Role(Base, RoleMixin, mixins.Timestamp):
    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(255))


role_user = db.Table(
    'role_user', db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('roles.id'))
)


class User(Base, UserMixin, mixins.Timestamp):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

    roles = db.relationship(
        'Role',
        secondary=role_user,
        backref=db.backref('users', lazy='dynamic')
    )
    boards = db.relationship(
        'Board', backref=db.backref('boards', lazy='dynamic')
    )


class Board(Base, mixins.Timestamp, mixins.SoftDelete):
    __tablename__ = 'boards'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    users = db.relationship(
        'User', backref=db.backref('users', lazy='dynamic')
    )


class BoardUser(Base):
    __tablename__ = 'board_user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    permission = db.Column(db.String(255), nullable=False)
    board_id = db.Column(db.Integer(), db.ForeignKey('boards.id'))
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

    board = db.relationship('Board', back_populates='users')
    user = db.relationship('User', back_populates='boards')
