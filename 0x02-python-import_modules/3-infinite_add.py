#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    result = 0
    argc = len(sys.argv) - 1
    while i <= argc:
        result = result + int(sys.argv[i])
        i = i + 1
    print(result)
