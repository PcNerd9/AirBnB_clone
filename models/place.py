#!/usr/bin/python3
"""contain only Place Class that inherit from the BaseModel class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Take the Place of the User

    Args:
        base_model (class): deals the manipulation of data
    """
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_id = []
    city_id = ""
    user_id = ""
    name = ""
    description = ""

    def __init__(self, *args, **kwargs):
        """initailizes Place Instance
        """
        super().__init__(*args, **kwargs)
