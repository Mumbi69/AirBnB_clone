#!/usr/bin/python3
"""Defines unittests for base_model module"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import models
import sys


class TestBaseModel(unittest.TestCase):
    """Testing the BaseModel class"""

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)


if __name__ == '__main__':
    unittest.main()
