#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    sum = 0
    value = 0
    new = 0
    values = []
    convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for letter in roman_string:
        for key in convert:
            if letter == key:
                values.append(convert[key])
                break

    while value < len(values):
        j = value + 1
        if j != len(values) and values[value] < values[j]:
            new = values[j] - values[value]
            value = value + 2
        else:
            new = values[value]
            value = value + 1
        sum += new
    return sum
