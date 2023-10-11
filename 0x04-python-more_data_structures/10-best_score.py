#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    list = []
    indcat = 0
    for key, value in a_dictionary.items():
        list.append(value)
    for i in range(0, len(list)):
        j = i + 1
        for j in range(0, len(list)):
            if list[j] > list[i]:
                indcat = 1
                break
            else:
                indcat = 0
        if indcat == 0:
            value = list[i]
    for key in a_dictionary:
        if a_dictionary[key] == value:
            return key
    return None
best_score({"Ahmed": 50, "Mod": 60})
