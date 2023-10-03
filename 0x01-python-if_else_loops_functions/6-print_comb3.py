#!/usr/bin/python3
for i in range(0, 8):
    for j in range(i + 1, 10):
        if j != i:
            if j > i:
                print("{}{}, ".format(i, j), end="")
            elif i > j:
                print("{}{}, ".format(j, i), end="")
print("89")
