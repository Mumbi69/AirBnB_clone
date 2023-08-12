#!/usr/bin/python3
""" unit test for bases"""
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models
import sys


class BaseModelTest(unittest.TestCase):
    """Testing the BaseModel class"""

    def test_class_doc(self):
        """Test ``BaseModel`` class for documentation"""
        self.assertIsNotNone(BaseModel.__doc__)


if __name__ == '__main__':
    unittest.main()
