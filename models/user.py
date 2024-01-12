#!/usr/bin/python3
# Scripts that deals with User info

from .base_model import BaseModel

class User(BaseModel):
    """_Take the infomation of the User

    Args:
        base_model (class): deals the manipulation of data
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
    def __init__(self, *args, **kwargs):
        """initialzing User Instance
        """
        super().__init__(*args, **kwargs)