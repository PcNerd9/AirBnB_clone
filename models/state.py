#!/usr/bin/python3
# Sripts that deals with the user State

from .base_model import BaseModel

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