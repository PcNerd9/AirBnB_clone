#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
"""
from cmd import Cmd
import models
from models.base_model import BaseModel
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User


class HBNBCommand(Cmd):
    prompt = "(hbnb) "
    user_list = {"BaseModel": BaseModel,
                 "State": State,
                 "City": City,
                 "Amenity": Amenity,
                 "Review": Review,
                 "Place": Place,
                 "User": User
                 }
    
    def do_create(self, line):
        if (line == ""):
            print("**class name missing**")
            return
        if (line not in self.user_list):
            print("**class doesn't exit**")
            return
        new_basemodel = self.user_list[line]()
        print(new_basemodel.id)
        new_basemodel.save()

    def search(self, line):
        if (line == ""):
            print("**class name missing**")
            return False
        param = line.split()
        if (param[0] not in self.user_list):
            print("**class doesn't exit**")
            return False
        if (len(param) == 1):
            print("**instance id missing**") 
            return False
        obj_id = ".".join([param[0], param[1]])

        all_objects = models.storage.all()
        for key in all_objects.keys():
            if (key == obj_id):
                return(all_objects[key])
            
    def do_show(self, line):
        obj = self.search(line)
        if (obj):
            print(obj)
        elif (obj == None):    
            print("**no instance found**")
        
    def do_destroy(self, line):
        if (line == ""):
            print("**class name missing**")
            return
        param = line.split()
        if (param[0]  not in self.user_list):
            print("** class doesn't exit **")
            return    
        if (len(param) == 1):
            print("** instance id missing **")
            return
        obj_id = ".".join([param[0], param[1]])
        all_objects = models.storage.all()
        for key in all_objects.keys():
            if (key == obj_id):
                del all_objects[key]
                models.storage.save()
                return
        print("** no instance found **")
    
    def do_all(self, line):
        if (line != "" and line not in self.user_list):
            print("** class doesn't exit **")
            return
        all_objects = models.storage.all()
        for key in all_objects.keys():
            print(all_objects[key])
                
    def do_update(self, line):
        if (line == ""):
            print("** class name missing **")
            return
        param = line.split()
        if (param[0] not in self.user_list):
            return    
        if (len(param) == 1):
            print("** instance id missing **")
            return
        if (len(param) == 2):
            print("** attribute name missing **")
            return
        if (len(param) == 3):
            print("** value missing **")
            return
        
        obj_id = ".".join([param[0], param[1]])
        all_objects = models.storage.all()
        for key in all_objects.keys():
            if (key == obj_id):
                setattr(all_objects[key], param[2], param[3])
                all_objects[key].save()
                return
        print("**no instance found**")    
                   
    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True
    
    def do_EOF(self, line):
        """exit the interpreter
        """
        return True
    def do_emptyline(self):
        """do nothing 
        """
        pass
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
