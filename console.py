#!/usr/bin/python3
"""Defines the program that contains the entry point of the CLI"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Representation of the class Cmd from the module cmd."""
    prompt = "[Air] "

    def emptyline(self):
        """Empty line that executes nothing"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self,line):
        """The end of file on input"""
        print("")
        return True

    def help_quit(self):
        """Help message for the quit command"""
        print("Quit command to exit the program")
        print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
