import os
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.ext.declarative import declarative_base


timeformat = "%Y-%m-%d,%H:%M:%S"

Base = declarative_base()

class BaseModel:
    """
        this is the base model for every instance
    """
    id = Column(String(50), primary_key=True, nullable=False)
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
        
    
    def to_dict(self):
        """ dictionary format for json conversion"""
        new_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
        new_dict['__class__'] = self.__class__.__name__
        return new_dict