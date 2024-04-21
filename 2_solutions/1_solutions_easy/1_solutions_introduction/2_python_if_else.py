#!/bin/python3


def is_weird(n: int) -> str:
    """
    Determines if a number is 'Weird' or 'Not Weird',
    based on specific conditions.
    """
    if 1 <= n <= 100:
        if n % 2 != 0:
            message = 'Weird'
        elif 2 <= n < 6:
            message = 'Not Weird'
        elif 6 <= n <= 20:
            message = 'Weird'
        else:  # This implies n > 20
            message = 'Not Weird'
    else:
        message = 'The number should be an integer between 1 and 100'

    return message


if __name__ == '__main__':
    n = int(input().strip())
    message = is_weird(n)
    print(message)
