#!/usr/bin/python3
"""Defines the program that contains the entry point of the CLI"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from shlex import split


class HBNBCommand(cmd.Cmd):
    """Representation of the class Cmd from the module cmd."""
    prompt = "(hbnb) "
    __classes = {
        "User"
        "State"
        "City"
        "Place"
        "Amenity"
        "Review"
    }

    def emptyline(self):
        """Empty line that executes nothing"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """The end of file on input"""
        print("")
        return True

    def help_quit(self):
        """Help message for the quit command"""
        print("Quit command to exit the program")
        print()

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it
           (to the JSON file) and prints the id
        """
        argl = parse(arg)
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """Displays the string representation of a class
           instance of a given id.
        """
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
