#!/usr/bin/python3
"""A script that to;
- take in a URL
- get  request to the URL and displays value
- of the X-Request-Id variable in the header of response
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    requests = urllib.request.Request(url)
    with urllib.request.urlopen(requests) as response:
        print(dict(response.headers).get("X-Request-Id"))
