#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_list = [0, 0]

    for x in range(2):
        if x < len(tuple_a):
            new_list[x] += tuple_a[x]
        if x < len(tuple_b):
            new_list[x] += tuple_b[x]
    return tuple(new_list)
