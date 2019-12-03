from flask import Blueprint
from flask_restful import Api
from app.resources.Hello import Hello
from app.resources.admin import Admin


api_blueprints = Blueprint('api', __name__)
admin_blueprints = Blueprint('admin', __name__)
api = Api(api_blueprints)
admin = Api(admin_blueprints)

# Routes
api.add_resource(Hello, '/hello')
admin.add_resource(Admin, '/123')