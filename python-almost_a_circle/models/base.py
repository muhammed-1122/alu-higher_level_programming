#!/usr/bin/python3
import json
import os

class Base:
    """Base class for managing id attribute and JSON serialization."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize Base instance.

        Args:
            id (int): The identity of the instance. If None, auto-incremented.
	"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert list of dictionaries to JSON string.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if not list_dictionaries or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances inheriting Base.
        """
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_objs = []
        dict_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert JSON string to list of dictionaries.

        Args:
            json_string (str): JSON string representation.

        Returns:
            list: List of dictionaries represented by json_string.
        """
        if not json_string or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set from dictionary.

        Args:
            **dictionary: Key/value pairs of attributes.

        Returns:
            Base: Instance with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load list of instances from a JSON file.

        Returns:
            list: List of instances loaded from file.
        """
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as f:
            json_str = f.read()
        dict_list = cls.from_json_string(json_str)
        return [cls.create(**d) for d in dict_list]
