#!/usr/bin/python3
"""contain only City Class that inherit from the BaseModel class
"""


from models.base_model import BaseModel


class City(BaseModel):
    """inherit from the BaseModel class
    """
    stated_id = None
    name = None
