#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_num = -999999
    for x in my_list:
        if x > max_num:
            max_num = x
    return max_num
