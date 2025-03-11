#!/usr/bin/python3
"""yes"""


class Student:
    """yes"""

    def __init__(self, first_name, last_name, age):
        """yes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """yes"""
        return self.__dict__
