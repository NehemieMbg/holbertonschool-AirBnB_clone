#!/usr/bin/python3
import uuid
from datetime import date, datetime
import models


class BaseModel:
    # initalazing current datetime to an attribute
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

    def __init__(self):
        """ Public instance attributes:"""
        # Assign id with an uuid string.
        self.id = str(uuid.uuid4())
        # datetime object: current datetime when created
        self.created_at = datetime.now()
        # datetime objec: current datetime when updated
        self.update_at = datetime.now()

    # Prints a string representation of the class object
    def __str__(self):
        """Prints a string representation of the class object"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the public instance attribute update at
        to the current datetime"""
        self.update_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        # creating a dic with __class as a key__
        # & the class name as its value
        dictionary = {"__class__": self.__class__.__name__}
        # looping through dict with items funciton to acces
        # the key and the value
        for key, value in self.__dict__.items():
            if key == "created_at":
                # converting the value if key is created_at
                dictionary[key] = value.isoformat()
            elif key == "updated_at":
                # converting the value if key is updated_at
                dictionary[key] = value.isoformat()
            else:
                dictionary[key] = value
        return dictionary
