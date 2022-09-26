#!/usr/bin/python3
def no_c(my_string):
    no_t = "Cc"

    for i in no_t:
        my_string = my_string.replace(i, "")
        return my_string
