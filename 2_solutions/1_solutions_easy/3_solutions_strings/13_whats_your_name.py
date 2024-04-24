#!/usr/bin/python3

def print_full_name(first: str, last: str) -> None:
    """
    Prints a greeting message with a full name,
    composed of the first and last name.
    """
    print(f'Hello {first} {last}! You just delved into python')


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    if len(first_name) <= 10 and len(last_name) <= 10:
        print_full_name(first_name, last_name)
    else:
        print('Names should be shorter than 10 characters each')
