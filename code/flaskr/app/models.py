import click

from datetime import datetime
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False
    )
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow
    )
    updated_at = db.Column(db.DateTime)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)


@click.command('init-db')
@with_appcontext
def init_db_command():
    '''Clear the existing data and create new tables.'''
    db.create_all()
    click.echo('Initialized the database.')


def init_app(app):
    db.init_app(app)
    app.cli.add_command(init_db_command)
