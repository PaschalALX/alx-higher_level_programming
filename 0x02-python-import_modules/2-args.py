#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    x = len(argv) - 1
    y = "argument"

    print('{} {}'.format(x, y+":")) \
        if x == 1 else print('{} {}'.format(x, y+'s.')) \
        if x == 0 else print('{} {}'.format(x, y+'s:'))
    [print('{}: {}'.format(z, argv[z])) for z in range(1, x + 1)]
