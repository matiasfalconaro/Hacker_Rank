#!/bin/python3


def manual_symmetric_difference(set_a, set_b):
    diff_a_to_b = set_a.difference(set_b)
    diff_b_to_a = set_b.difference(set_a)
    for num in sorted(diff_a_to_b.union(diff_b_to_a)):
        print(num)

if __name__ == "__main__":
    first_set = set(map(int, input().split(',')))
    second_set = set(map(int, input().split(',')))
    result = manual_symmetric_difference(first_set, second_set)
