#!/usr/bin/python3
"""contain only Review Class that inherit from the BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Take the Review of the User

    Args:
        base_model (class): deals the manipulation of data
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initailizes Review Instance
        """
        super().__init__(*args, **kwargs)
