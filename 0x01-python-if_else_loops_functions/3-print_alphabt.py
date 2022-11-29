#!/usr/bin/python3

[print("{}".format(chr(x)), end="")
    for x in range(97, 123) if x != ord("q") and x != ord("e")]
