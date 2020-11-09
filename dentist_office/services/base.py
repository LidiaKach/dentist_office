from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

from dentist_office.models import db
from dentist_office.exceptions import AppException


class Base:
    model_class = None

    @classmethod
    def create(cls, data_dict):
        obj = cls.model_class(**data_dict)
        try:
            db.session.add(obj)
            db.session.commit()
        except IntegrityError as e:
            raise AppException(f'{cls.model_class.__name__} with that {data_dict} already exists.')
        return obj

    @classmethod
    def delete(cls, obj):
        db.session.delete(obj)
        db.session.commit()

    @classmethod
    def get_by_id(cls, obj_id):
        try:
            result = cls.model_class.query.filter_by(id=obj_id).one()
        except MultipleResultsFound as e:
            raise AppException('Multiple rows were found.')

        except NoResultFound as e:
            raise AppException(f'{cls.model_class.__name__} with id = {obj_id} does not exist.', 404)

        return result

    @classmethod
    def update(cls, obj, data):
        for k, v in data.items():
            setattr(obj, k, v)
        try:
            db.session.commit()
        except IntegrityError as e:
            raise AppException(f'{cls.model_class.__name__} with that {data} already exists.')
        return obj
