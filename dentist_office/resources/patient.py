from dentist_office.models.patient import Patient, PatientSchema
from dentist_office.models import db
from dentist_office.services.patient import PatientService

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

patients_schema = PatientSchema(many=True)
patient_schema = PatientSchema()


class PatientResourceList(Resource):
    def get(self):
        patients = Patient.query.all()
        patients = patients_schema.dump(patients)
        return {'data': patients}, 200

    def post(self):
        json_data = request.get_json(force=True)

        try:
            data = patient_schema.load(json_data)
        except ValidationError as err:
            return {'errors': err.messages}, 400

        patient = PatientService.create(data)
        result = patient_schema.dump(patient)
        return result, 201


class PatientResource(Resource):
    def get(self, id):
        result = PatientService.get_by_id(id)
        result = patient_schema.dump(result)
        return result, 200

    def put(self, id):
        result = PatientService.get_by_id(id)

        json_data = request.get_json(force=True)

        try:
            data = patient_schema.load(json_data, partial=('first_name', 'last_name', 'email',))
        except ValidationError as err:
            return {'errors': err.messages}, 400

        result = PatientService.update(result, data)
        result = patient_schema.dump(result)

        return result, 200

    def delete(self, id):
        result = PatientService.get_by_id(id)
        PatientService.delete(result)
        return {'message': 'Patient has been deleted'}, 200
