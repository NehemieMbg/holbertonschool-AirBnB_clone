#!/usr/bin/python3
from base_model import BaseModel


class User(BaseModel):
    """Class that inherits form BaseModel"""
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""
