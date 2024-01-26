#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
if __name__ == "__main__":
    import urllib.request
    import sys
    data = {"email": sys.argv[2]}
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode("utf-8")
    print(the_page)
