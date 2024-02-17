#!/bin/python3

def previous_integers(n: int) -> None:
    """Prints all previous nonnegative integers from a given integer"""
    for i in range(1, n + 1):
        print(i, end="")

if __name__ == '__main__':
    n = int(input())
    previous_integers(n)