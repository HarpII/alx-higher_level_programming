#!/usr/bin/python3

def no_c(my_string):
    result_string = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            result_string = result_string + ""
        else:
            result_string = result_string + i
    return (result_string)
