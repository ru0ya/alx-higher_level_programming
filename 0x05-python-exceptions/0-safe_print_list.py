#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    for i in range(x):
        try:
            print(my_list[i], end="\n")
            a += 1
        except ValueError:
            break
        print()
    return (a)
