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


if __name__ == "__main__":
    unittest.main()
