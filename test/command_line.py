#!/usr/bin/python3

import cmd

class MyCmd(cmd.Cmd):
    def do_hello(self, line):
        """Print a greeting."""
        print("Hello, world!")

    def do_quit(self, line):
        """Exit the command interpreter."""
        return True

if __name__ == '__main__':
    my_cmd = MyCmd()
    my_cmd.cmdloop()  # Start the command interpreter loop
