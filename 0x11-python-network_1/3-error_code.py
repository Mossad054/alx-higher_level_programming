#!/usr/bin/python3
""" Request to a URL and displays the response body
  - Handles HTTP errors.
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    rqst = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(rqst) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
