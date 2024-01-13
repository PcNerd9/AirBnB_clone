#!/usr/bin/python3
"""contain only City Class that inherit from the BaseModel class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Take the City of the User

    Args:
        base_model (_type_): _description_
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Take the City of the User

        Args:
            base_model (_type_): _description_
        """
        # pass all the arguments to the base class
        super().__init__(*args, **kwargs)
