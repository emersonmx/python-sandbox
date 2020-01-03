import os


def init_app(app, test_config=None):
    app.config.from_mapping(
        SECRET_KEY='dev',
        SECURITY_PASSWORD_SALT='dev',
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
