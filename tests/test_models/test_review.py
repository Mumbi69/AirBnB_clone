#!/usr/bin/python3
"""Defines unittests for review class"""

import os
import models
import unittest
from datetime import datetime
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Represents testing of the Review class"""
    def test_no_args(self):
        self.assertEqual(Review, type(Review()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_two_reviews_unique_ids(self):
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.id, r2.id)


if __name__ == "__main__":
    unittest.main()
