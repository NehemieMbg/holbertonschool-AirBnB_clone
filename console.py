#!/usr/bin/python3
import cmd



class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    intro = "Type something!"
    def do_exit(self, inp):
        """Exit the application"""
        print("Bye")
        return True

    def help_exit(self):
        print('exit the application. Shrothand: x q Ctrl-D.')

    def do_add(self, inp):
        print("Adding '{}'".format(inp))
    
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
 