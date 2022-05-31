#!/usr/bin/python3


def uppercase(str):
    new_str = ""

    for i in range(0, len(str)):
        char_to_digit = ord(str[i])
        if char_to_digit >= 97 and char_to_digit <= 122:
            char_to_digit -= 32

        new_str += chr(char_to_digit)
    print("{}".format(new_str))
    return(new_str)
