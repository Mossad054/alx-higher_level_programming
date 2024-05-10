#!/usr/bin/python3
"""A script that;
- takes in a URL
- send request to URL & displays the value
- of  X-Request-Id variable  in the header response.
"""

import sys
import requests


if __name__ == "__main__":
    # get  url from the command line
    url = sys.argv[1]
    email = sys.argv[2]

    # create a dict with the email param
    data = {'email': email}

    # send POST request to the URL
    response = requests.post(url, data=data)
    print(response.text)
