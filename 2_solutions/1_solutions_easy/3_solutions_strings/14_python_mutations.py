#!/bin/python3

def mutate_string(string: str, position: int, character: str) -> str:
    """Modifies a given string by replacing the character at a specified position with a new character."""
    l = list(string)
    l[position] = character
    s_new = ''.join(l) 
    # Another approach
    # l = string[:5] + "k" + string[6:]
    return s_new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)