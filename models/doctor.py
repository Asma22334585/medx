
#from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey, Column, String, Integer
from models.base_model import Base, BaseModel
from hashlib import md5

class Doctor(Base, BaseModel):
    __tablename__ = "DOCTOR"

    username = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    fullname = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    location = Column(String(128), nullable=False)
    speciality = Column(String(128), nullable=False)
    degree = Column(String(128), nullable=False)
    license = Column(String(128), nullable=False)
    status = Column(String(10), nullable=False)
    availability = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes a user"""
        super().__init__(*args, **kwargs)
    
    def __setattr__(self, name, value):
        """hasshing password before saving"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__init__(name, value)