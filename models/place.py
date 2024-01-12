#!/usr/bin/python3
# Sripts that deals with the user Place

from .base_model import BaseModel

class Place(BaseModel):
    """Take the Place of the User

    Args:
        base_model (class): deals the manipulation of data
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude =  ""
    longitude = ""
    amenity_ids = ""
    
    def __init__(self, *args, **kwargs):
        """initailizes Place Instance
        """
        super().__init__(*args, **kwargs)