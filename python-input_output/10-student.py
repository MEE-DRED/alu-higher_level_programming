#!/usr/bin/python3
"""class Student that defines a student by: (based on 9-student.py)
Public instance attributes"""


class Student:
    """ Class to create student instances """

    def __init__(self, first_name, last_name, age):
        """ Special method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that returns directory description """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            d_list = {}                                                                                                         
            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        d_list[satr] = obj[satr]
                        return d_list
                    return obj
