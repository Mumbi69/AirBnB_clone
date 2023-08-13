#!/usr/bin/python3
"""Defines unittests for state class"""

import os
import models
import unittest
from datetime import datetime
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Represents testing of the State class"""
    def test_no_args(self):
        self.assertEqual(State, type(State()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_two_states_unique_ids(self):
        st1 = State()
        st2 = State()
        self.assertNotEqual(st1.id, st2.id)


if __name__ == "__main__":
    unittest.main()
