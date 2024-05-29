from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import models
from models.base_model import Base, BaseModel
from models.user import User
from models.record import Record
from models.doctor import Doctor

classes = {
           "User": User,
           "Record": Record,
           "Doctor": Doctor
           }

class DbStorage:
    """interaction with databse"""
    __engine = None
    __session = None

    def __init__(self):
        """at the instantiation"""
        MEDX_MYSQL_USER = "medx" #getenv("MEDX_MYSQL_USER")
        MEDX_MYSQL_PWD = "betty" #getenv("MEDX_MYSQL_PWD")
        MEDX_MYSQL_HOST = "localhost" #getenv("MEDX_MYSQL_HOST")
        MEDX_MYSQL_DB = "medx" #getenv("MEDX_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(MEDX_MYSQL_USER,
                                             MEDX_MYSQL_PWD,
                                             MEDX_MYSQL_HOST,
                                             MEDX_MYSQL_DB
                                             )
                                        )
    
    def new(self):
        """create a new instance to the database"""
        self.__session.add(self)
    
    def all(self, cls=None):
        """return all instance from the database"""
        new_dict = {}
        for c in classes:
            if cls is None or c is classes[c] or c is cls:
                objs = self.__session.query(classes[c]).all()
                for obj in objs:
                    key = self.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj
        return new_dict
    
    def save(self):
        """save an instance to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an instance from databse"""
        if obj:
            self.___session.delete(obj) 

    def reload(self):
        """ reload the databases and updates any change"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """close a object session"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None