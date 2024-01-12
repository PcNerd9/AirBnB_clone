#!/usr/bin/python3
# Scripts that deals with City State

from .base_model import BaseModel

class City(BaseModel):
    """Take the City of the User

    Args:
        base_model (_type_): _description_
    """
    state_id = ""
    name = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
