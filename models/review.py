#!/usr/bin/python3
"""9.More classes"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class with public attributes
    that inherits from Basemodel"""
    place_id = ""
    user_id = ""
    text = ""
