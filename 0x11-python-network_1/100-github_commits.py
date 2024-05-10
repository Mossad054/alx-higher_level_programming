#!/usr/bin/python3
"""list 10 most recent commits on a given  repository
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[1], sys.argv[2])

    request = requests.get(url)
    commits = request.json()
    try:
        for i in range(10):
        #prints the list
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass


