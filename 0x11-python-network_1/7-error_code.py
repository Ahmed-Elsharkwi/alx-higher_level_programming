#!/usr/bin/python3
"""
script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user with the
letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(" http://0.0.0.0:5000/search_user")
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
