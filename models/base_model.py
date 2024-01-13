#!/usr/bin/python3
#Scripts that deals with the Class [BaseModel]
#That also create the dict for all object for
#serialization and deserialization


from datetime import datetime
import json
import models
from uuid import uuid4


class BaseModel():
    """Handles the serialization and deserialization of the object
    """

    def __init__(self, *arg, **kwargs):
        """initialize the BaseModel
        """
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

    def save(self):
        """_summary_: saves the object to a file in form of json
        """
        models.storage.new(self)
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """_summary_: returns the dictionary representation of an instance
        """
        new_dict = {key: value for key, value in self.__dict__.items()}
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def __str__(self):
        """ Retuns a string representation of an instance
        Returns:
            _type_:__str__
        """
        return f"[{self.__class__.__name__}], ({self.id}), {self.__dict__}"
