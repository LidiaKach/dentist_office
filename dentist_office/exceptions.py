from werkzeug.exceptions import HTTPException
import json
from flask import Response


class AppException(HTTPException):
    def __init__(self, message, code=400):
        super().__init__(message,
                         Response(json.dumps({'message': message}), content_type='application/json', status=code))
