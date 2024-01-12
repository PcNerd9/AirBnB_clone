#!/usr/bin/python3
# Scripts that tests for User

import sys
import unittest
sys.path.append("../../")
from models import user, state, city, place, review, amenity
User = user.User
State = state.State
City = city.City
Amenity = amenity.Amenity
Place = place.Place
Review = review.Review

class TestModels(unittest.TestCase):
    def setUp(self):
        # Create instances for testing ifr all the classes
        self.user = User(
            email="test@example.com",
            password="password123",
            first_name="John",
            last_name="Doe"
                         )
        self.state = State(name="California")
        self.city = City(state_id="1", name="San Francisco")
        self.amenity = Amenity(name="WiFi")
        self.place = Place(city_id="1", user_id="1", name="Cozy Apartment")
        self.review = Review(place_id="1", user_id="1", text="Great stay!")
    
    def test_user_attributes(self):
        """Test for the user entries
        """
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
    
    def test_state_attributes(self):
        """ Test for the state user entris
        """
        self.assertEqual(self.state.name, "California")

    def test_city_attributes(self):
        """Test for all the City entries
        """
        self.assertEqual(self.city.state_id, "1")
        self.assertEqual(self.city.name, "San Francisco")

    def test_amenity_attributes(self):
        """Test for all amenity entries
        """
        self.assertEqual(self.amenity.name, "WiFi")

    def test_place_attributes(self):
        """Test for all place entries
        """
        self.assertEqual(self.place.city_id, "1")
        self.assertEqual(self.place.user_id, "1")
        self.assertEqual(self.place.name, "Cozy Apartment")

    def test_review_attributes(self):
        """Tests for all review entries
        """
        self.assertEqual(self.review.place_id, "1")
        self.assertEqual(self.review.user_id, "1")
        self.assertEqual(self.review.text, "Great stay!")
        
if __name__ == "__main__":
    unittest.main()