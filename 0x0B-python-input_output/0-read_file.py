#!/usr/bin/python3
""" Python input and output module. """


def read_file(filename=""):
    """A function that reads a text file with
    Utf-8 encoding"""

    with open(filename, 'r', encoding="Utf-8") as f:
        f.read()
