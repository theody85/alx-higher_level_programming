#!/usr/bin/python3
""" A Class Module that defines a student
by certain qualities. """


class Student:
    """defines a student by certain qualities"""

    def __init__(self, first_name, last_name, age):
        """Instantiates first_name, last_name and age of an instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is not None:
            li = {}
            for a in attrs:
                if a is in self.__dict__:
                    li[a] = self.__dict__[a]
            return li
        return self.__dict__
