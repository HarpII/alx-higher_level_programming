#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new = []
    for i in my_list:
        new.append(i)
    for j in range(len(new)):
        if new[j] == search:
            new[j] = replace

    return (new)

