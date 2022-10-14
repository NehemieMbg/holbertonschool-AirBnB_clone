#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    def __init__(self):
        """Private class attribute"""
        # Path of the file
        self.__file_path = "file.json"
        # Empty dictionary
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        serial_dict = {}
        for key in self.__objects.keys():
            serial_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w+") as jsonData:
            json.dump(serial_dict, jsonData)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r+") as data:
                jsonData = json.load(data)
                for key, value in jsonData.items():
                    # eval function to reconstruct an object
                    self.__objects[key] = eval(value['__class__'])(**value)
        # Get all exceptions possible
        except Exception:
            pass
