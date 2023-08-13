#!/usr/bin/python3
"""Defines unittests for place module"""

import os
import models
import unittest
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """Represents testing of the Place class."""
    def test_no_args(self):
        self.assertEqual(Place, type(Place()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_two_places_unique_ids(self):
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)


if __name__ == "__main__":
    unittest.main()
