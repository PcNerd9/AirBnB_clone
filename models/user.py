#!/usr/bin/python3
"""contain only State Class that inherit from the BaseModel class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """inherit from the BaseModel class
    """
    email = None
    password = None
    first_name = None
    last_name = None
