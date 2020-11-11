from flask import Flask

from dentist_office.config import DevelopmentConfig


def create_app(config_class):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(config_class)

    from dentist_office.models import db
    db.init_app(app)

    from dentist_office.app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app


if __name__ == '__main__':
    app = create_app(DevelopmentConfig)
    app.run('0.0.0.0')
