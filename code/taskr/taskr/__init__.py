from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_security import Security, SQLAlchemyUserDatastore
from flask_wtf.csrf import CSRFProtect

from taskr import config

db = SQLAlchemy()
migrate = Migrate()

security = Security()
csrf = CSRFProtect()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    config.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    from taskr import models
    user_datastore = SQLAlchemyUserDatastore(db, models.User, None)
    security.init_app(app, user_datastore)

    csrf.init_app(app)

    from taskr import jinja2
    jinja2.init_app(app)

    @app.route('/')
    def index():
        from flask import render_template
        return render_template('index.html')

    return app
