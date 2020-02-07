from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()

csrf = CSRFProtect()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    from . import config
    config.init_app(app, test_config)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models  # noqa

    from . import jinja2
    jinja2.init_app(app)

    csrf.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
