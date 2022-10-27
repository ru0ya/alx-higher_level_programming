#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = my_list.copy()
    if idx < 0:
        return n
    elif idx >= (len(my_list)-1):
        return n
    else:
        n[idx] = element
        return n

