#!/usr/bin/python3
'''
Write a Python script that takes in a URL, sends a request
to the URL and displays the body of the response
(decoded in utf-8).
'''
from urllib import request, error
from sys import argv

if (__name__ == "__main__"):
    if len(argv) == 2:
        url = argv[1]
        req_ojb = request.Request(url)
        try:
            with request.urlopen(req_obj) as req:
                print(req.read().decode('utf-8'))
        except error.HTTPError as e:
            print('Error: {}'.format(e.code))