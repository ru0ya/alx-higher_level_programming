#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = my_list.copy()
    if idx < 0:
        return n
    if idx >= len(my_list):
        return n

        n[idx] = element
        return n

