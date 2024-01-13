#!/usr/bin/python3
"""contain only Amenity Class that inherit from the BaseModel class
"""
from models.base_model import BaseModel



class Amenity(BaseModel):
    """inherit from the BaseModel class
    Args:
        base_model (class): deals the manipulation of data
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """initailizes Amenity Instance
        """
        super().__init__(*args, **kwargs)
