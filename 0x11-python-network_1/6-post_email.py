#!/usr/bin/python3
'''
Write a Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
Request Module
'''
import requests
from sys import argv

if (__name__ == "__main__"):
    if len(argv) == 3:
        url = argv[1]
        res = requests.post(url, data={'email': argv[2]})
        print(res.text)
