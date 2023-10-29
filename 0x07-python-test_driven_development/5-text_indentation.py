#!/usr/bin/python3
"""
print two new line after each chracter from those chracter : ? .
the type of text variable should be stirng
otherwise raise Type Error
There should be no space at the beginning or at the end of each printed line
"""


def text_indentation(text):
    if type(text) is not str or text is None:
        raise TypeError("text must be a string")
    else:
        li_text = text.split(" ")
        for i in range(0, len(li_text)):
            if '?' in li_text[i] or '.' in li_text[i] or ':' in li_text[i]:
                print(li_text[i])
                print()
            else:
                result = i + 1
                print("{}".format(li_text[i]), end="")
                if result != len(li_text):
                    print(" ", end="")
