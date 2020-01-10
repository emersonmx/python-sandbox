from .helpers import mix


def init_app(app):
    app.jinja_env.globals.update(mix=mix)
