#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        the_page = response.headers
    print(the_page["X-Request-Id"])
