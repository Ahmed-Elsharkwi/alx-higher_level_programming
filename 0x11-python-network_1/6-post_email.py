#!/usr/bin/python3
"""
script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user with the
letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    import sys

    info = {email: sys.argv[2]}
    r = requests.post(sys.argv[1], data=info)
    print(r.text)
