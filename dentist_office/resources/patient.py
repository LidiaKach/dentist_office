from flask_restful import Resource
from flask import jsonify, make_response


class Patient(Resource):
    def get(self):
        return {"message": "Hello, World!"}


#    return make_response(jsonify('Test response'), 200)
