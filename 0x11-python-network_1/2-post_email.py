#!/usr/bin/python3
'''
Write a Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
'''
from urllib import request
from sys import argv

if (__name__ == "__main__"):
    if len(argv) == 3:
        url = "{}?email={}".format(argv[1], argv[2])
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
