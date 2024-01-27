#!/usr/bin/python3
""" 
script that takes in a letter and 
sends a POST request to http://0.0.0.0:5000/search_user with the 
letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    import sys

    q=""
    if sys.argv[1] is not None:
        q = sys.argv[1]
    r = requests.post(" http://0.0.0.0:5000/search_user", data=q)
    print(r)
