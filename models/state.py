#!/usr/bin/python3
"""contain only State Class that inherit from the BaseModel class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Take the State of the User

    Args:
        base_model (class): deals the manipulation of data
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """initailizes State Instance
        """
        super().__init__(*args, **kwargs)
