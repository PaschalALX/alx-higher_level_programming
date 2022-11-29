#!/usr/bin/python3

[print("{:02}".format(x), end=", ")
    if x < 99 else print("{}".format(x), end="\n")
    for x in range(0, 100)]
