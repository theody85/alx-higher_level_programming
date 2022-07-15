#!/usr/bin/python3
""" A Class Module """


class Student:
    """defines a student by certain qualities"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            li = {}
            for a in attrs:
                if a is in self.__dict__:
                    li[a] = self.__dict__[a]
            return li
        return self.__dict__

    def reload_from_json(self, json):
        for i in json:
            self.__dict__[i] = json[i]