#!/usr/bin/python3
"""
This module contains basic required functions
for all the classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """The main class where all other classes inherit from"""

    def __init__(self, *args, **kwargs):
        """
        defines unique id for an instance
        and keeps track of the time of their
        creation and update
        """
        for key, value in kwargs.items():
            if key != '__class__':
                if key == 'updated_at' or key == 'created_at':
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)

        from models import storage
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(args) == 0:
            storage.new(self)
        else:
            storage.new(self)

    def __str__(self):
        """
        Returns a string rep of our object
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        """
        update public instance attribute updated_at
        with current date
        """
        self.updated_at = datetime.utcnow()
        from models import storage
        storage.save()

    def to_dict(self):
        """
        returns a dictionary of all attributes of the class instance
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()

        return instance_dict
