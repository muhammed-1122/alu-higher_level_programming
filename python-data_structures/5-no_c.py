#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    new_str = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_str += ch
    return new_str
