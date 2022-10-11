#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    def __init__(self):
        """Private class attribute"""
        self.__file_path = "file.json"
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
                self.__object[key] = eval(value['__class__'](**value))
        except Exception:
            pass
