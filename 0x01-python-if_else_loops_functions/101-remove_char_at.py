#!/usr/bin/python3

def remove_char_at(str, n):
    str_list = list()
    for i in range(len(str)):
        if not (i == n):
            str_list.append(str[i])
    return (''.join(str_list))
