#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    bool_list = []

    [bool_list.append(True) if (x % 2) == 0
        else bool_list.append(False) for x in my_list]

    return bool_list
