#!/usr/bin/python3
""" A script to;
- fetch https://alx-intranet.hbtn.io/status
- use urlib package
"""

from urllib import request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    # fetch URL
    with request.urlopen(url) as response:
        # Read & decode  response body
        response_body = response.read()

        # show response body.
        print("Body response:")
        print("\t- type: {}".format(type(response_body)))
        print("\t- content: {}".format(response_body))
        print("\t- utf8 content: {}".format(response_body.decode('utf-8')))
