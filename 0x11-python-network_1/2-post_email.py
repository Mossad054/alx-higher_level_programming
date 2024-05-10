#!/usr/bin/python3
"""using urllib to send POST request"""

import sys
from urllib import request
from urllib import parse

if __name__ == "__main__":
    # Get  URL ,email from the command line.
    url = sys.argv[1]
    email = sys.argv[2]

    # Create  dict with the email 
    input_data = {'email': email}

    # Encode data  sent in the request body
    data_encoded = parse.urlencode(data).encode('ascii')

    # Make a POST request to the provided URL with the email par.
    with request.urlopen(url, input_data=data_encoded) as response:
        #decode the response body in utf-8
        print(response.read().decode('utf-8'))
