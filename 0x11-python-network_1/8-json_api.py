#!/usr/bin/python3
"""
Write a Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    q = argv[1][0] if len(argv) == 2 else ""
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data={'q': q})
    try:
        json = r.json()
        if not json:
            print("No result")
        else:
            print("[{}] {}".format(json.get('id'), json.get('name')))
    except ValueError as e:
        print("Not a valid JSON")
