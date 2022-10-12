#!/usr/bin/python3
"""
Imports:
cmd: Library that provides a command line interface
for an application.
It has interactive she with comman completition and history
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command Interpreter"""
    prompt = '(hbnb) '
    intro = "Type something!"

    def do_quit(self, inp):
        """
        Exit the application
        """
        return True

    def do_EOF(self):
        return True

    def empty_line(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

