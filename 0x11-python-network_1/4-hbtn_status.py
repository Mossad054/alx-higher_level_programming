#!/usr/bin/python3
"""fetch https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    rqst = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(rqst.text)))
    print("\t- content: {}".format(rqst.text))
