#!/bin/usr/python3
"""
"""

import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


class FileStorage:
    __file_path = "datafile.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        new_obj = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[new_obj] = obj

    def save(self):
        my_json = {}
        for key, value in self.__objects.items():
            my_json[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(my_json, f, indent=2)

    def reload(self):
        user_list = {"BaseModel": BaseModel,
                     "State": State,
                     "City": City,
                     "Amenity": Amenity,
                     "Review": Review,
                     "Place": Place,
                     "User": User
                     }
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
                for key, value in self.__objects.items():
                    obj = key.split(".")[0]

                    self.__objects[key] = user_list[obj](**value)
        except FileNotFoundError:
            pass
