from . import auth


def init_app(app):
    app.add_url_rule('/', view_func=auth.dashboard, endpoint='dashboard')
    app.add_url_rule('/login', view_func=auth.login, endpoint='login')
    app.add_url_rule('/logout', view_func=auth.logout, endpoint='logout')
