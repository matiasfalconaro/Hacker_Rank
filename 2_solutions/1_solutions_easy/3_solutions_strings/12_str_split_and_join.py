#!/usr/bin/python3

def split_and_join(line: str) -> str:
    """
    Splits a string on spaces, then joins the elements with a hyphen.
    """
    line = line.split(' ')
    line = "-".join(line)
    return line


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
