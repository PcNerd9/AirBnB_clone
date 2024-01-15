#!/usr/bin/python3
"""
Contain Classes to test the FileStorage Class
"""
import json
from unittest import TestCase
from models import FileStorage
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorageInitialization(TestCase):
    """
    Test the  correct initialization of the FileStorage
    """
    def test_file_class_type(self):
        """
        test the type of the class
        """
        file_storage = FileStorage()
        self.assertEqual(type(file_storage), FileStorage)

    def test_filestorage_class_private_file_path(self):
        """
        test the corrrect type of file_path private attribute
        """
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_filestorage_class_private_objects(self):
        """
        test the correct type of the objects private attribute
        """
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_filestorage_all_method_return_type(self):
        """
        test whether the all method returns the correct type
        """
        self.assertEqual(dict, type(FileStorage().all()))


class TestFileStorageMethod(TestCase):
    """
    test the return type of all method and the value
    of the __objects private attribute is the same
    """
    def test_filestorage_all_is___objects(self):
        self.assertEqual(FileStorage._FileStorage__objects,
                         FileStorage().all())

    def test_filestorage_all_with_arg(self):
        """
        test the all method with argument
        """
        with self.assertRaises(TypeError):
            FileStorage().all(None)

    def test_filestorage_new(self):
        """
        test whether the new method correctly create
        the key, value pair and add it to the
        __object private attribute
        """
        base = BaseModel()
        user = User()
        place = Place()
        city = City()
        review = Review()
        state = State()
        amenity = Amenity()
        base_key = "BaseModel.{}".format(base.id)
        user_key = "User.{}".format(user.id)
        place_key = "Place.{}".format(place.id)
        city_key = "City.{}".format(city.id)
        review_key = "Review.{}".format(review.id)
        state_key = "State.{}".format(state.id)
        amenity_key = "Amenity.{}".format(amenity.id)
        all_object = models.storage.all()
        self.assertTrue(base_key in all_object)
        self.assertTrue(user_key in all_object)
        self.assertTrue(place_key in all_object)
        self.assertTrue(city_key in all_object)
        self.assertTrue(review_key in all_object)
        self.assertTrue(state_key in all_object)
        self.assertTrue(amenity_key in all_object)

    def test_filestorage_new_arg(self):
        """
        test the new method with argument
        """
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_filestorage_save(self):
        """
        test whether the save method correctly save the
        newly created object to the json file
        """
        base = BaseModel()
        user = User()
        place = Place()
        city = City()
        review = Review()
        state = State()
        amenity = Amenity()
        base_key = "BaseModel.{}".format(base.id)
        user_key = "User.{}".format(user.id)
        place_key = "Place.{}".format(place.id)
        city_key = "City.{}".format(city.id)
        review_key = "Review.{}".format(review.id)
        state_key = "State.{}".format(state.id)
        amenity_key = "Amenity.{}".format(amenity.id)
        base_dict = base.to_dict()
        user_dict = user.to_dict()
        place_dict = place.to_dict()
        city_dict = city.to_dict()
        review_dict = review.to_dict()
        state_dict = state.to_dict()
        amenity_dict = amenity.to_dict()
        base.save()
        user.save()
        place.save()
        city.save()
        review.save()
        state.save()
        amenity.save()
        my_dict = models.storage.all()
        self.assertTrue(base_key in my_dict)
        self.assertTrue(user_key in my_dict)
        self.assertTrue(place_key in my_dict)
        self.assertTrue(city_key in my_dict)
        self.assertTrue(review_key in my_dict)
        self.assertTrue(state_key in my_dict)
        self.assertTrue(amenity_key in my_dict)

    def test_save_with_arg(self):
        """
        test the save method with an argument
        """
        with assertRaises(TypeError):
            models.storage.save(None)
