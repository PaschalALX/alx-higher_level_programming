#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display
your id
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) == 3:
        username = argv[1]
        password = argv[2]
        url = "https://api.github.com/user"
        headers = {
            "Accept": "application/vnd.github+json"
        }

        res = requests.get(url, auth=(username, password), headers=headers)
        print(res.json().get('id'))
