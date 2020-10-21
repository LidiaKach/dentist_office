from flask import Flask



def create_app(config_filename):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from dentist_office.models import db
    db.init_app(app)

    from dentist_office.app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app('dentist_office.config')
    app.run('0.0.0.0')

