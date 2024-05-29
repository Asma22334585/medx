"""User Module"""
from hashlib import md5
from sqlalchemy import String, Column, DateTime, Integer
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class User(BaseModel):
    """user class"""
    __tablename__ = "users"
    #id = Column(String(50), nullable=False, unique=True, primary_key=True)
    fullname = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    dob = Column(DateTime, nullable=False)
    blood_group = Column(String(50), nullable=True)
    genotype = Column(String(50), nullable=True)
    allergies = Column(String(50), nullable=True, default=None)
    weight = Column(Integer(), nullable=True)
    location = Column(String(50), nullable=True)

    def __init__(self, *args, **kwargs):
        """instantiation of obj"""
        super().__init__(*args, *kwargs)
    
    '''def __setattr__(self, name, value):
        """hashing of password"""
        if name == "password":
            value = md5(value.encode().hexdigest())
        super().__init__(name, value)'''