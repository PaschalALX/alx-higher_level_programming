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
    try:
        res = requests.get(argv[1])
        print(res.text)
    except res.HTTPError as e:
        print("Error code: {}".format(e))
