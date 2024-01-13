#!/usr/bin/python3
"""
Contains a single class (HBNBCommand) which uses the Cmd class
as the base class to implement the python command line interpreter
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
    """Implement the python commmand line interpreter using the
    Cmd class as the base class
    """
    prompt = "(hbnb) "
    __user_list = {"BaseModel": BaseModel,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Review": Review,
                   "Place": Place,
                   "User": User
                   }

    def do_create(self, line):
        """Create <Class Name> create a new class with the class name
        """
        if (line == ""):
            print("** class name missing **")
            return
        if (line not in self.__user_list):
            print("** class doesn't exit **")
            return
        new_basemodel = self.__user_list[line]()
        print(new_basemodel.id)
        new_basemodel.save()

    def search(self, line):
        """search for an instance with Class name and id
        Args:
            line (_type_): the instance of the class found

        Returns:
            _type_: _description_
        """
        if (line == ""):
            print("** class name missing **")
            return False
        param = line.split()
        if (param[0] not in self.__user_list):
            print("** class doesn't exit **")
            return False
        if (len(param) == 1):
            print("** instance id missing **")
            return False
        obj_id = ".".join([param[0], param[1]])

        all_objects = models.storage.all()
        for key in all_objects.keys():
            if (key == obj_id):
                return all_objects[key]

    def do_show(self, line):
        """Show <Class Name> <id> print the string representation
        of an instance based on the class name and id
        """
        obj = self.search(line)
        if (obj):
            print(obj)
        elif (obj is None):
            print("** no instance found **")

    def do_destroy(self, line):
        """Destroy <Class Name> <id> deletes an instance based on the
        class name and id then save the changes
        """
        if (line == ""):
            print("** class name missing **")
            return
        param = line.split()
        if (param[0] not in self.__user_list):
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
        """All <Class Name> print all string representation of all instances
        based or not on the class name: Ex. (HBNB) all BaseModel or (HBNB) all
        """
        if (line != "" and line not in self.__user_list):
            print("** class doesn't exit **")
            return
        all_objects = models.storage.all()
        list_object = [str(value) for value in all_objects.values()]
        print(list_object)

    def do_update(self, line):
        """Update <Class Name> <id> updates an instance based
        on the class name and id
        by adding or updating attribute
        """
        if (line == ""):
            print("** class name missing **")
            return
        line = line.replace('"', '')
        param = line.split()
        if (param[0] not in self.__user_list):
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
        print(line)
        obj_id = ".".join([param[0], param[1]])
        all_objects = models.storage.all()
        for key in all_objects.keys():
            if (key == obj_id):
                setattr(all_objects[key], param[2], str(param[3]))
                all_objects[key].save()
                return
        print("** no instance found **")

    def all(self, arg):
        """
        <Class Name>.all() returns a list of all the
        <Class Name> in the storage
        """
        splitted_arg = arg.split()
        obj = splitted_arg[0]
        if (obj not in self.__user_list):
            print("** no instance found **")
            return
        all_objects = models.storage.all()
        all_obj = [str(all_objects[key]) for key in
                   all_objects.keys() if key.startswith(obj)]
        print(all_obj)

    def count(self, arg):
        """
        <Class Name>.count() return the number of
        times the <Class Name> is present in the storage
        """
        splitted_arg = arg.split()
        obj = splitted_arg[0]
        if (obj not in self.__user_list):
            print("** no instance found **")
            return
        number = 0
        all_objects = models.storage.all()
        for key in all_objects.keys():
            if key.startswith(obj):
                number += 1
        print(number)

    def parse_command(self, command):
        """
        parse the command in form of
        <Class Name>.<Command>('arguments')
        and return a tuple (<command>, '<Class Name> argument
        ')
        """
        if ("." not in command):
            return None
        command_list = command.split(".")
        command_value = command_list[1].replace('(', " ")
        command_value = command_value.replace(')', " ")
        command_value = command_value.replace(",", '')
        command_value = command_value.split()
        command = command_value[0]
        argument = command_value[1:]
        instance = command_list[0]
        argument = " ".join(argument)
        argument = argument.replace('"', '')
        argument = " ".join([instance, argument])
        return (command, argument)

    def default(self, line):
        """
        Handles command that a passed in form of
        <Class Name>.<command('argument(s)') and
        non-existing commands
        """
        commands = {
            "all": self.all,
            "count": self.count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update

        }
        parsed_line = self.parse_command(line)
        if (parsed_line is None):
            return Cmd.default(self, line)
        if (parsed_line[0] not in commands):
            return Cmd.default(self, parsed_line[0])
        commands[parsed_line[0]](parsed_line[1])
        return

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """exit the interpreter
        """
        print()
        return True

    def do_emptyline(self):
        """do nothing
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
