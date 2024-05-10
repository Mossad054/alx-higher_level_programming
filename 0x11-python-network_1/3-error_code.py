#!/usr/bin/python3
""" script that;
- takes in a URL
- displays body of the response (decoded in utf-8).
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

## Make a GET request to the URL
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        # Handle HTTP errors and print the HTTP status.
        print("Error code: {}".format(e.code))

