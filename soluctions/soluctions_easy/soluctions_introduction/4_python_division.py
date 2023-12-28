#!/bin/python3

def division(a, b):
    int_division = a//b
    float_division = a/b
    return int_division, float_division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if b > 0:
        int_division, float_division = division(a, b)
        print(int_division)
        print(float_division)
    else:
        print("The second number should be a positive integer")