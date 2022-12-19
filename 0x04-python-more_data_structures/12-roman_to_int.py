#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string == None:
        return (0)
    
    integer = 0
    roman_milestones = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for i, j in zip(roman_string, roman_string[1:]):
        if i not in roman_milestones.keys():
            return (0)
        elif roman_milestones[i] >= roman_milestones[j]:
            integer += roman_milestones[i]
        else:
            integer -= roman_milestones[i]
    integer += roman_milestones[roman_string[-1]]

    return (integer)
