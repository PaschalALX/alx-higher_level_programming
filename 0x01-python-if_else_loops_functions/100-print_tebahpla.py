#!/usr/bin/python3

[print(chr(abs(c)), end="")
    if not (abs(c) % 2)
    else print(chr(abs(c) - 32), end="") for c in range(-122, -96)]
