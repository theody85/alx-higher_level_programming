#!/use/bin/python3
"""Python input and output module"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns
    the number of characters written"""
    with open(filename, 'w', encoding="Utf-8") as f:
        f.write(text)
