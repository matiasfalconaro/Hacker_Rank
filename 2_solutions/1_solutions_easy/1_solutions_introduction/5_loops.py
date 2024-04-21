#!/bin/python3

def square_non_negative_int(n: int) -> None:
    """
    For all non-negative integers , i < n print i^2.
    """
    for i in range(n):
        print(i**2)


if __name__ == '__main__':
    n = int(input())
    square_non_negative_int(n)
