from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    from app import config
    config.init_app(app)

    from app import db
    db.init_app(app)

    from app import auth
    app.register_blueprint(auth.bp)
    from app import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
