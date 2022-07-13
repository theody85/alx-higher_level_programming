#!/usr/bin/python3
"""Class Module"""


class Student:
    """defines a student by certain qualities"""

    def __init__(self, first_name, last_name, age):
        """Instantiates first_name, last_name and age of an instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return(self.__dict__)
