#!/usr/bin/python3
"""A script to;
- take in a URL and send request to the URL
- display body of the response
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        #decode Errors
        print("Error code: {}".format(r.status_code))
    else:
    # print the output
        print(r.text)
