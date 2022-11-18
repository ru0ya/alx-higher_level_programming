#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_n = 0
    for k in range(len(roman_string)):
        if k > 0 and roman_d[roman_string[k]] > roman_d[roman_string[k - 1]]:
            roman_n += roman_d[roman_string[k]] - 2 * \
                    roman_d[roman_string[k - 1]]
        else:
            roman_n += roman_d[roman_string[k]]
    return roman_n
