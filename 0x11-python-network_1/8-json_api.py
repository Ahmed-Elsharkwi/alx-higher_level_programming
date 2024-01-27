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
    if len(sys.argv[1]) == 2:
        q = sys.argv[1]
    r = requests.post(" http://0.0.0.0:5000/search_user", data=q)
    
    try:
        data = r.json()
        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(data["id"], data["name"]))
    except ValueError:
        print("Not a valid JSON")
