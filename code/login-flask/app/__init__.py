from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    from . import config
    config.init_app(app, test_config)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models # noqa

    @app.route('/')
    def index():
        return 'Hello world!'

    return app
