#!/user/bin/python3
"""9.More classes"""
from models.base_model import BaseModel


class City(BaseModel):
    """class with public attributes
    that inherits from Basemodel"""
    state_id = ""
    name = ""
