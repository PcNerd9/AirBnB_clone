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
        self.user = User()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.place = Place()
        self.review = Review()

    def test_user_attributes(self):
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_state_attributes(self):
        self.assertTrue(hasattr(self.state, "name"))

    def test_city_attributes(self):
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "state_id"))

    def test_amenity_attributes(self):
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_place_attributes(self):
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))

    def test_review_attributes(self):
        self.assertTrue(hasattr(self.review, "text"))
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))

    def test_user_string_representation(self):
        self.assertEqual(
            str(self.user),
            f"[{self.user.__class__.__name__}] ({self.user.id}) {self.user.__dict__}"
        )

    def test_state_string_representation(self):
        self.assertEqual(
            str(self.state),
            f"[{self.state.__class__.__name__}] ({self.state.id}) {self.state.__dict__}"
        )

    def test_city_string_representation(self):
        self.assertEqual(
            str(self.city),
            f"[{self.city.__class__.__name__}] ({self.city.id}) {self.city.__dict__}"
        )

    def test_amenity_string_representation(self):
        self.assertEqual(
            str(self.amenity),
            f"[{self.amenity.__class__.__name__}] ({self.amenity.id}) {self.amenity.__dict__}"
        )

    def test_place_string_representation(self):
        self.assertEqual(
            str(self.place),
            f"[{self.place.__class__.__name__}] ({self.place.id}) {self.place.__dict__}"
        )

    def test_review_string_representation(self):
        self.assertEqual(
            str(self.review),
            f"[{self.review.__class__.__name__}] ({self.review.id}) {self.review.__dict__}"
        )


if __name__ == '__main__':
    unittest.main()
