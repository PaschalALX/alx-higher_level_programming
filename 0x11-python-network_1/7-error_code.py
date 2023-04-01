#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a
request to the URL and displays the body of the
response (decoded in utf-8).
Request Module
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    res = requests.get(argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
