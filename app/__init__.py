from flask import Flask
# from .extensions import *
from mongoengine import *


def create_app():
    app = Flask(__name__)
    app.debug = True

    connect(
        'flask-blueprint-test',
        host='mongodb://localhost/flask-blueprint-test'
    )

    from app.api import api_blueprints,admin_blueprints
    app.register_blueprint(api_blueprints, url_prefix='/api')
    app.register_blueprint(admin_blueprints, url_prefix ='/admin')

    return app





