#!/usr/bin/python3
'''
    Write a Python script that takes in a URL, sends a request to
    the URL and displays the value of the X-Request-Id variable
    found in the header of the response.
    (Request Module)
'''
if (__name__ == "__main__"):
    import requests
    from sys import argv

    if len(argv) == 2:
        response = requests.get(argv[1])
        print(response.headers['X-Request-Id'])
