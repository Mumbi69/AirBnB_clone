#!/usr/bin/python3
"""
This module contains methods for object storage using
json object
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from pathlib import Path


class FileStorage:
    """serializes instances to a JSON file and deserializes
       JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(FileStorage):
        """function returns the dictionary __objects"""
        return FileStorage.__objects

    def new(FileStorage, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(FileStorage):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_data = {}

        for key, obj in FileStorage.__objects.items():
            obj_data[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_data, file)

    def reload(FileStorage):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_data = json.load(file)
                for key, value in obj_data.items():
                    class_name = value['__class__']
                    obj = eval(class_name + '(**value)')
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            """
            ignore :)
            """
