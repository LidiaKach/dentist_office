from dentist_office.services.base import Base
from dentist_office.models.patient import Patient


class PatientService(Base):
    model_class = Patient
