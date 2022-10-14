#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """Class that inherits form BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
