#!/usr/bin/python3

from typing import Optional, Tuple


def arithmetic_operator(a: int, b: int) -> Optional[Tuple[int, int, int]]:
    """
    Performs basic arithmetic operations:
    Addition, subtraction, multiplication) on two integers.
    """
    if 1 <= a <= 10**10 and 1 <= b <= 10**10:
        addition = a + b
        subtraction = a - b
        multiplication = a * b
        return addition, subtraction, multiplication
    else:
        return None


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    result = arithmetic_operator(a, b)
    if result:
        addition, subtraction, multiplication = result
        print(addition)
        print(subtraction)
        print(multiplication)
    else:
        print('The numbers should be integers between 1 and 10^10')
