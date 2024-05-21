from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey, Column, String, Integer

Base = declarative_base()

class doctor(Base):
    __tablename__ = "DOCTOR"

    username = Column("username", String(128), nullable=False)
    password = Column("pwd", String(128), nullable=False)
    fullname = Column("fname", String(128), nullable=False)
    email = Column("email", String(128), nullable=False)
    location = Column("location", String(128), nullable=False)
    speciality = Column("speciality", String(128), nullable=False)
    degree = Column("degree", String(128), nullable=False)
    license = Column("license", String(128), nullable=False)
    status = Column("status", String(10), nullable=False)
    availability = Column("availability", String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes a user"""
        super().__init__(*args, **kwargs)
