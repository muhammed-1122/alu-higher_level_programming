#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if my_list is None or idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
