#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
                    
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0

    for char in reversed(roman_string):
        if char in roman_dict:
            value = roman_dict[char]
            if value >= prev_value:
                total += value
            else:
                total -= value
        prev_value = value
        else:
            return 0  # Invalid character

    return total

