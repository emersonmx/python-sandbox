import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

bcrypt = Bcrypt()
db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    _setup_config(app)

    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    return app


def _setup_config(app, test_config=None):
    app.config.from_mapping(
        SECRET_KEY='dev',
        BCRYPT_HANDLE_LONG_PASSWORDS=True,
        SQLALCHEMY_DATABASE_URI='sqlite:///{}'.format(
            os.path.join(app.instance_path, 'taskr.sqlite')
        ),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    os.makedirs(app.instance_path, exist_ok=True)
