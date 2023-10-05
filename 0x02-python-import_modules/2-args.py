#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    i = 1
    if argc == 1:
        arg = "{} argument:".format(argc)
    elif argc == 0:
        arg = "{} arguments.".format(argc)
    else:
        arg = "{} arguments:".format(argc)
    print(arg)
    while i <= argc:
        print("{}: {}".format(i, sys.argv[i]))
        i = i + 1
