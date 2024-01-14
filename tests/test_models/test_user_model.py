#!/usr/bin/python3
# Scripts that tests for User

import unittest
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
        class_name = self.user.__class__.__name__
        class_id = self.user.id
        class_dict = self.user.__dict__
        self.assertEqual(
            str(self.user),
            f"[{class_name}] ({class_id}) {class_dict}"
        )

    def test_state_string_representation(self):
        class_name = self.state.__class__.__name__
        class_id = self.state.id
        class_dict = self.state.__dict__
        self.assertEqual(
            str(self.state),
            f"[{class_name}] ({class_id}) {class_dict}"
        )

    def test_city_string_representation(self):
        class_name = self.city.__class__.__name__
        class_id = self.city.id
        class_dict = self.city.__dict__
        self.assertEqual(
            str(self.city),
            f"[{class_name}] ({class_id}) {class_dict}"
        )

    def test_amenity_string_representation(self):
        class_name = self.amenity.__class__.__name__
        class_id = self.amenity.id
        class_dict = self.amenity.__dict__
        self.assertEqual(
            str(self.amenity),
            f"[{class_name}] ({class_id}) {class_dict}"
        )

    def test_place_string_representation(self):
        class_name = self.place.__class__.__name__
        class_id = self.place.id
        class_dict = self.place.__dict__
        self.assertEqual(
            str(self.place),
            f"[{class_name}] ({class_id}) {class_dict}"
        )

    def test_review_string_representation(self):
        class_name = self.review.__class__.__name__
        class_id = self.review.id
        class_dict = self.review.__dict__
        self.assertEqual(
            str(self.review),
            f"[{class_name}] ({class_id}) {class_dict}"
        )


if __name__ == '__main__':
    unittest.main()
