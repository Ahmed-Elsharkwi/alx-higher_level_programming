#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
if __name__ == "__main__":
    import requests
    import sys

    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
