#!/usr/bin/python3
"""
Write a Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) <= 1:
        print("No result")
    else:
        url = "http://0.0.0.0:5000/search_user"
        r = requests.post(url, data={'q': argv[1]})
        try:
            json = r.json()
            print("[{}] {}".format(json['id'], json['name']))
        except requests.exceptions.JSONDecodeError as e:
            print("Not a valid JSON")
