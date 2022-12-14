#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:

    def __init__(self, *args, **kwargs):
        """ Public instance attributes:"""
        # datetime object: current datetime when created & updated
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        # Assign id with an uuid string.
        self.id = str(uuid.uuid4())

        for key, value in kwargs.items():
            if key in ["created_at", "updated_at"]:
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
            elif key != "__class__":
                setattr(self, key, value)
        models.storage.new(self)

    # Prints a string representation of the class object
    def __str__(self):
        """Prints a string representation of the class object"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the public instance attribute update at
        to the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        # new dictionary
        dictionary = {"__class__": self.__class__.__name__}
        # loop in dict to acces the key and value
        for key, value in self.__dict__.items():
            # converting the value if key is created_at or updated_at
            if key == "created_at" or key == "updated_at":
                dictionary[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                dictionary[key] = value
        return dictionary
