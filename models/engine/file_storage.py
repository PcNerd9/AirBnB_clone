#!/bin/usr/python3
"""
"""

import json
from datetime import datetime
from models.base_model import BaseModel
class FileStorage:
    __file_path = "file.json"
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
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
                for key, value in self.__objects.items():
                    self.__objects[key] = BaseModel(**value)                
        except: 
            pass
        
