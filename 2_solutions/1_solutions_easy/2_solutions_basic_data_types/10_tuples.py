#!/bin/python3

def get_t(n, elements):

    t = tuple(map(int, elements.split()))
    return hash(t)

if __name__ == '__main__':
    n = int(input().strip())
    elements = input().strip()
    print(get_t(n, elements))
