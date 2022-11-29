#!/usr/bin/python3

def uppercase(str):
    for x in str:
        if not (ord(x) >= 65 and ord(x) <= 90):
            if (ord(x) >= 97 and ord(x) <= 122):
                x = chr(ord(x) - 32)
        print("{}".format(x), end='')
    print("{}".format(''), end='\n')
