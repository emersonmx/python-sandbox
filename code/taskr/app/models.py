from flask_security import UserMixin, RoleMixin
from sqlalchemy_mixins import AllFeaturesMixin

from app import db
from app import mixins


class Base(db.Model, AllFeaturesMixin):
    __abstract__ = True


role_user = db.Table(
    'role_user', db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('roles.id'))
)


class Role(Base, RoleMixin, mixins.Timestamp):
    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(255))


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
