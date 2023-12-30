#!/bin/python3

def swap_case(s: str) -> str:
    "Converts all lowercase letters to uppercase letters and vice versa."
    new_string = ''
    for character in s:
        if character.isupper():
            new_string += character.lower()
        else:
            new_string += character.upper()
    return new_string

if __name__ == '__main__':
    s = input()
    print(swap_case(s))
if __name__ == '__main__':
    s = input()
    print(swap_case(s))