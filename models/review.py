#!/usr/bin/python3
"""Defines the class review that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents the class Review"""

    place_id = ""
    user_id = ""
    text = ""
