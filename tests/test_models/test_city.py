#!/usr/bin/python3
"""Defines unittests for city module."""

import os
import models
import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """Testing of the City class."""
    def test_no_arg(self):
        self.assertEqual(City, type(City()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_state_id_is_public_class_attribute(self):
        cy = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cy))
        self.assertNotIn("state_id", cy.__dict__)

    def test_name_is_public_class_attribute(self):
        cy = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cy))
        self.assertNotIn("name", cy.__dict__)

    def test_two_cities_unique_ids(self):
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)


if __name__ == "__main__":
    unittest.main()
