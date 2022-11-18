#!/usr/bin/python3
def complex_delete(my_dict, value):
    for idx in list(my_dict.keys()):
        if my_dict[idx] == value:
            del my_dict[idx]
    return my_dict
