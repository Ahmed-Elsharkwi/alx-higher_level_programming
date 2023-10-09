#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        tuple_a = (len(sentence), None)
    else:
        tuple_a = (len(sentence), sentence[0])
    return tuple_a
