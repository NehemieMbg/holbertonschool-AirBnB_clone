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

    def do_exit(self, inp):
        """Exit the application"""
        print("Bye")
        return True

    def help_quit(self):
        """Provides help documentation for 'quit'"""
        print('exit the application. Shrothand: x q Ctrl-D.')

    def help_add(slef):
        print("Add a new entry to the system.")

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)

        print("Default: {}".format(inp))

    do_EOF = do_exit
    help_EOF = help_exit

    def do_add(self, inp):
        print("Adding '{}'".format(inp))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
