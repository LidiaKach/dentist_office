from flask import Blueprint
from flask_restful import Api

from dentist_office.resources.patient import PatientResource, PatientResourceList




api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(PatientResourceList, '/patient')
api.add_resource(PatientResource, '/patient/<int:id>', endpoint='patient')


