#!/usr/bin/python3
"""
Imports:
cmd: Library that provides a command line interface
for an application.
It has interactive she with comman completition and history
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command Interpreter"""
    prompt = '(hbnb) '
    classes = {"BaseModel"}

    def do_quit(self, inp):
        """
        Exit the application
        """
        return True

    def do_EOF(self):
        return True

    def emptyline(self):
        """Print an empty line"""
        pass
    
    def do_create(self, inp):
        if len(inp) == 0:
            print("** class name missing **")
        elif inp not in self.classes:
            print("** class doesn't exist **")
        else:
            # ask why eval(inp)()
            newInstance = eval(inp)()
            newInstance.save()
            print(newInstance.id)

    def do_show(self, inp):
        if len(inp) == 0:
            print("** class name missing **")
            return
        parse = inp.split()
        if parse[0] not in self.classes:
            print("** class doesn't exist **")
            return
        try:
            if parse[1]:
                name = f"{parse[0]}.{parse[1]}"
                if name not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_all(self, inp):
        parse = inp.split()
        if parse[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            lst = []
            allDict = storage.all()
            for val in allDict.values():
                if val.__class__.__name__ == parse[0]:
                    lst.append(str(val))
            print(lst)

    def destroy(self, inp):
        # To be continued
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
