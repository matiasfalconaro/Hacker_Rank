#!/bin/python3

def capitalize(name, capitalized_name, first_letter):
    for letter in name:
        if first_letter:
            letter = letter.upper()
            first_letter = False
            capitalized_name += letter
        elif letter == " ":
            capitalized_name += letter
            first_letter = True
        else:
            capitalized_name += letter
    return capitalized_name


if __name__ == "__main__":
    name = input()
    capitalized_name = ""
    first_letter = True
    print(capitalize(name, capitalized_name, first_letter))
