#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments to retrieve commits
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{1}/{0}/commits"
    url = url.format(repo, owner)
    headers = {
        "Accept": "application/vnd.github+json"
    }

    res = requests.get(url, params={"per_page": 10})
    for record in res.json():
        sha = record["sha"]
        username = record["commit"]["author"]["name"]
        print("{}: {}".format(sha, username))
