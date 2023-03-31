#!/usr/bin/python3
'''
    Write a Python script that takes in a URL, sends a request to
    the URL and displays the value of the X-Request-Id variable
    found in the header of the response.
'''
if (__name__ == "__main__"):
    from urllib import request
    from sys import argv

    if len(argv) == 2:
        with request.urlopen(argv[1]) as response:
            print(response.getheader('X-Request-Id'))
