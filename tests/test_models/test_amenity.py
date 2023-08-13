#!/usr/bin/python3
"""Defines unittests for amenity class"""

import os
import models
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Represents testing instantiation of the Amenity class"""
    def test_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_two_amenities_unique_ids(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_args_unused(self):
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())


if __name__ == "__main__":
    unittest.main()
