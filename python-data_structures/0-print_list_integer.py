#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list is None:
        return
    for number in my_list:
        if isinstance(number, int):
            print("{:d}".format(number))
