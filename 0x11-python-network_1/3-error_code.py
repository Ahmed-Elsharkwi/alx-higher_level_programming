#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
if __name__ == "__main__":
    import urllib.request
    import sys
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            the_page = response.read().decode("utf-8")
            print(the_page)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
