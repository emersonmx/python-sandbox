from . import helpers


def init_app(app):
    app.jinja_env.globals.update(mix=helpers.mix)
