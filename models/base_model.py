import os
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.ext.declarative import declarative_base


timeformat = "%Y-%m-%d,%H:%M:%S"

Base = declarative_base()

class BaseModel(Base):
    """
        this is the base model for every instance
    """
    __abstract__ = True
    id = Column(String(50), primary_key=True, unique=True, nullable=False)
    created_at = Column(DATETIME, nullable=False)
    update_at = Column(DATETIME, nullable=False)

    def __init__(self, *args, **kwargs):
        """ params at instatiation """
        if kwargs:
            for key, value in kwargs.items:
                if key != '__class__':
                    setattr(self, key, value)
            if kwargs.get('created_at', None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs['created_at'], timeformat)
            else:
                self.created_at = datetime.now()

            if kwargs.get('updated_at', None) and type(self.update_at) is str:
                self.update_at = datetime.strptime(kwargs['update_at'], timeformat)
            else:
                self.update_at = datetime.now()
            if kwargs.get('id', None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.update_at = self.created_at

    def save(self):
        """save every instance to database and updating the time"""
        self.update_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
        
    
    def to_dict(self, save_fs=None):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(timeformat)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(timeformat)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if save_fs is None:
            if "password" in new_dict:
                del new_dict["password"]
        return new_dict
    
    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)