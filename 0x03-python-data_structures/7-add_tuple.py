#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    zipped = zip(tuple_a, tuple_b)
    mapped = map(sum,zipped)
    x = tuple(mapped)
    return x
