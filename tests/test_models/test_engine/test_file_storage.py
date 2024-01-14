#!/usr/bin/python3
"""
"""
from unittest import TestCase
from models import FileStorage
import models
from models.base_model import BaseModel 

class TestFileStorageInitialization(TestCase):
    def test_file_class_type(self):
        file_storage =    FileStorage()
        self.assertEqual(type(file_storage), FileStorage)

    def test_filestorage_class_private_file_path(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        
    def test_filestorage_class_private_objects(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
    
    def test_filestorage_all_method_return_type(self):
        self.assertEqual(dict, type(FileStorage().all()))
class TestFileStorageMethod(TestCase):        
    def test_filestorage_all_is___objects_classattribute(self):
        self.assertEqual(FileStorage._FileStorage__objects, FileStorage().all())
        
    def test_filestorage_all_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage().all(None)
           
    def test_filestorage_new(self):
        base = BaseModel()
        base_key = "BaseModel.{}".format(base.id)
        all_object = models.storage.all()
        self.assertTrue(base_key in all_object) 