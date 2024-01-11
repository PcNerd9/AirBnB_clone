#!/usr/bin/python3

from datetime import datetime
import json
import models
from uuid import uuid4

class BaseModel():
    def __init__(self, *arg, **kwargs):
        if (kwargs):
            for key, value in kwargs.items():
                if (key == "__class__"):
                    continue
                else:
                    setattr(self, key, value)
            self.created_at = datetime.fromisoformat(self.created_at)
            self.updated_at = datetime.fromisoformat(self.updated_at)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            
    def save(self):
        """_summary_
        saves the object to a file in form of json 
        """
        self.updated_at = datetime.now()
        models.storage.save()
        
        
    def to_dict(self):
        """_summary_:
             
        Returns:
            _type_: a dictionary representation of the obj 
        """
        new_dict = {key: value for key, value in self.__dict__.items()}
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
    def __str__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)
