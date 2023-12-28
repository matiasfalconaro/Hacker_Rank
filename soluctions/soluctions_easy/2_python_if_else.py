#!/bin/python3

import math
import os
import random
import re
import sys

def is_weird(n):
    if n >= 1 and n <= 100:
        if n %2 != 0:
            message = 'Weird'
        elif n %2 == 0 and n in range(2,6):
            message = 'Not Weird'
        elif n %2 == 0 and n in range(6,21):
            message = 'Weird'
        elif n %2 == 0 and n >= 20:
            message = 'Not Weird'
    else:
        message = 'The number should be an integer between 1 and 100'
    return message

if __name__ == '__main__':
    n = int(input().strip())
    message = is_weird(n)
    print(message)
    