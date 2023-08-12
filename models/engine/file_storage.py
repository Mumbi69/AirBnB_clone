#!/usr/bin/python3
"""
This module contains methods for object storage using
json object
"""
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(FileStorage):
        return FileStorage.__objects

    def new(FileStorage, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(FileStorage):
        obj_data = {}

        for key, obj in FileStorage.__objects.items():
            obj_data[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_data, file)

    def reload(FileStorage):
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
