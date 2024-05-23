import datetime
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel

class Record(Base, BaseModel):
    """creates the medical record module"""
    __tablename__ = "records"
    id = Column(String(70), nullable=False, unique=True, primary_key=True)
    doctor_notes = Column(String(4000), nullable=True)
    diagnosis = Column(String(4000), nullable=True)
    prescription = Column(String(4000), nullable=True)
    user_id = Column(String(50), ForeignKey('User.id'))
    doctor_id = Column(String(50), ForeignKey('Doctor.id')) 

    def __init__(self, *args, **kwargs):
        """constructor method"""
        super().__init__(*args, **kwargs)

    #def to_dict(self):
     #   """Return dictionary format of object"""
     #   new_dict = {
     #               key: (value.isoformat() if isinstance(value, datetime.datetime) else value)
     #               for key, value in self.__dict__.items()
     #               }
     #   new_dict['__class__'] = self.__class__.__name__
     #   return new_dict