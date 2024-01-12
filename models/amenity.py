#!/usr/bin/python3
# Sripts that deals with the user amenity

from .base_model import BaseModel

class Amenity(BaseModel):
    """Take the Amenity of the User

    Args:
        base_model (class): deals the manipulation of data
    """
    name = ""
    
    def __init__(self, *args, **kwargs):
        """initailizes Amenity Instance
        """
        super().__init__(*args, **kwargs)