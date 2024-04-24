#!/usr/bin/python3

# Read input from STDIN. Print output to STDOUT

def print_hackerrank_logo(thickness):
    # Top Cone
    for i in range(thickness):
        print(('H' * i).rjust(thickness-1) + 'H' + ('H' * i).ljust(thickness-1))

    # Top Pillars
    for i in range(thickness+1):
        print(('H' * thickness).center(thickness*2) + ('H' * thickness).center(thickness*6))

    # Middle Belt
    for i in range((thickness+1)//2):
        print(('H' * thickness * 5).center(thickness*6))    

    # Bottom Pillars
    for i in range(thickness+1):
        print(('H' * thickness).center(thickness*2) + ('H' * thickness).center(thickness*6))    

    # Bottom Cone
    for i in range(thickness):
        print((('H' * (thickness-i-1)).rjust(thickness) + 'H' + ('H' * (thickness-i-1)).ljust(thickness)).rjust(thickness*6))

if __name__ == '__main__':
    thickness = int(input())
    if thickness % 2 == 1:
        print_hackerrank_logo(thickness)
    else:
        print("Thickness must be an odd number.")
