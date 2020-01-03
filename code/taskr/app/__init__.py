from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_security import Security, SQLAlchemyUserDatastore

from app import config

db = SQLAlchemy()
migrate = Migrate()

security = Security()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    config.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    from app import models
    user_datastore = SQLAlchemyUserDatastore(db, models.User, None)
    security.init_app(app, user_datastore)

    return app
