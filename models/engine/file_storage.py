#!/usr/bin/python3
"""
This module contains methods for object storage using
json object
"""
import json


class FileStorage:

    def __init__(self, file_path="file.json"):
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(
                obj.__class__.__name__, obj.id
                )
        self.__objects[key] = obj

    def save(self):
        obj_data = {}
        try:
            with open(self.__file_path, 'r') as file:
                obj_data = json.load(file)
        except FileNotFoundError:
            pass

        for key, obj in self.__objects.items():
            obj_data[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(obj_data, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                obj_data = json.load(file)
                for key, value in obj_data.items():
                    class_name = value['__class__']
                    obj = eval(class_name + '(**value)')
                    self.__objects[key] = obj
        except FileNotFoundError:
            """
            ignore :)
            """
            pass
