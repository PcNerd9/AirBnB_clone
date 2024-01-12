#!/usr/bin/python3
# Scripts that test my base_model_1

from sys import path
import unittest
from io import StringIO
from unittest.mock import patch
from datetime import datetime
path.append('../../')
from models.base_model import BaseModel


class TestBaseModel_1(unittest.TestCase):

    def setUp(self):
        # creates an instance of BaseModel

        self.instance = BaseModel()

    def test_public_attribute_existence(self):
        # checks for all public attributes in the instannce (BaseModel)

        self.assertTrue(hasattr(self.instance, "id"))
        self.assertTrue(hasattr(self.instance, "created_at"))
        self.assertTrue(hasattr(self.instance, "updated_at"))

    def test_default_values(self):
        # checks for the default types of the attribute in (BaseModel)

        self.assertIsInstance(self.instance.id, str)
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)
    
    def test_magic_method_str(self):
        # checks the return of __str__ magic method
        expected_output = f"[BaseModel] ({self.instance.id}) {self.instance.__dict__}"
        self.assertEqual(str(self.instance), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_for_save_method(self, mock_stdout):
        # checks if the time is correctly updated
        with patch('models.storage.save') as mock_save:
            self.instance.save()
            mock_save.assert_called_once()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')

        prevTime = self.instance.updated_at
        self.instance.save()
        self.assertNotEqual(prevTime, self.instance.updated_at)

    def test_for_to_dict_method(self):
        # checks the types of the diction ary retured by the method (BaseModel)

        object_dict = self.instance.to_dict()

        self.assertIsInstance(object_dict, dict)
        self.assertIn("__class__", object_dict)
        self.assertIn('id', object_dict)
        self.assertIn('created_at', object_dict)
        self.assertIn('updated_at', object_dict)
        self.assertEqual(object_dict['__class__'], 'BaseModel')
        self.assertIsInstance(object_dict['id'], str)
        self.assertTrue(datetime.fromisoformat(object_dict['created_at']))
        self.assertTrue(datetime.fromisoformat(object_dict['updated_at']))
        
    
if __name__ == "__main__":
    unittest.main()
