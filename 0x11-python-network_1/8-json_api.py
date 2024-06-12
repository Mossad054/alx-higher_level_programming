#!/usr/bin/python3
"""A script to;
- take in a letter and sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    data = {"q": letter}

    rqst = requests.post("http://0.0.0.0:5000/search_user", data)
    try:
        response = rqst.json()
        if response == {}:
        #prints requests results
            print("No result")
        else:
        # print the outsof hthe  request.
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
