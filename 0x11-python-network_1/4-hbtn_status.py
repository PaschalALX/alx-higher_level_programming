#!/usr/bin/python3
'''
Write a Python script that fetches https://alx-intranet.hbtn.io/status
(Request Module)
'''

if __name__ == "__main__":
    import request
    url = "https://alx-intranet.hbtn.io/status"
    res = request(url)
    print("Body response:")
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))
