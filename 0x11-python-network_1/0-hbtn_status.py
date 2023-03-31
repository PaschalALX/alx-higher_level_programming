#!/usr/bin/python3
'''
Write a Python script that fetches https://alx-intranet.hbtn.io/status
'''
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        res = response.read()
        _type = type(res)
        _utf8 = res.decode('utf-8')

        print("Body response:{3} type: {1}{3} content: {0}{3} utf8: {2}"
              .format(res, _type, _utf8, '\n    -'))
	
