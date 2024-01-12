#!/usr/bin/python3
# Sripts that deals with the user Review

from .base_model import BaseModel
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