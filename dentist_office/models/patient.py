from dentist_office.models import db

from flask import Flask
from marshmallow import Schema, fields, pre_load, validate, ValidationError
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120))
    street = db.Column(db.String(120))

    def __repr__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class PatientSchema(ma.Schema):
    id = fields.Integer()
    email = fields.Email(required=True)
    first_name = fields.String(required=True, validate=validate.Length(min=1))
    last_name = fields.String(required=True, validate=validate.Length(min=1))
    phone = fields.String(required=True, validate=validate.Length(min=10, max=12))
    city = fields.String(allow_none=True)
    street = fields.String(allow_none=True)
