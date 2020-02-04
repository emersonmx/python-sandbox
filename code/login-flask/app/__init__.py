from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    from . import config
    config.init_app(app, test_config)

    @app.route('/')
    def index():
        return 'Hello world!'

    return app
