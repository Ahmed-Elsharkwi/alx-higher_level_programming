#!/usr/bin/python3
def islower(c):
    if c == "":
        raise ValueError
    if c >= 'a' and c <= 'z':
        return True
    else:
        return False
