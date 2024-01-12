#!/usr/bin/python3
"""contain only Review Class that inherit from the BaseModel class 
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """inherit from the BaseModel class
    """
    place_id = None
    user_id = None
    text = None