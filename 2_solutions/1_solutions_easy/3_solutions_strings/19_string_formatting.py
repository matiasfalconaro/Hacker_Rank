#!/bin/python3

def print_formatted(number):
    spacing = len(format(number, 'b'))
    for i in range(1,number+1):
        print (f"{i:>{spacing}} {i:>{spacing}o} {i:>{spacing}X} {i:>{spacing}b}")
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)