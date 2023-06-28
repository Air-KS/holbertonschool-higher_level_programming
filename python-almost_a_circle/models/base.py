#!/usr/bin/python3
"""Defines a base model class."""
import json


class Base:
    """Represent the base model.

    Represents the "base" for all other classes in project 0x0C*.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns JSON string representation of list dict """
        if list_dictionaries is None:
            list_dictionaries = []
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save json strings of all instances into file """
        objs = []
        if list_objs is not None:
            for obj in list_objs:
                objs.append(cls.to_dictionary(obj))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as files:
            files.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """ Returns Python obj of JSON string representation """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns instance with attributes already set """
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns list of instances """
        filenamee = cls.__name__ + ".json"
        load = []
        try:
            with open(filenamee, "r") as f:
                instances = cls.from_json_string(f.read())
            for index, dic in enumerate(instances):
                load.append(cls.create(**instances[index]))
        except:
            pass
        return load
