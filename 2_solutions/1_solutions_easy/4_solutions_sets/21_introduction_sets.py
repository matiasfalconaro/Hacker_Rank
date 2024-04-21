#!/bin/python3

def set_maker(arr: str, N: int) -> set:
    heights = []
    if N > 0 and N <= 100:
        for i in range(N):
            height = int(arr[i])
            heights.append(height)
        return set(map(int, heights))
    else:
        print('Las alturas deben ser positivas y menores o iguales a 100')


def average(set_heights: set) -> int:
    if not set_heights:
        return 0.0
    average_height = sum(set_heights)/len(set_heights)
    return round(average_height, 3)


if __name__ == "__main__":
    N = int(input()) # arr size
    if N == 0:
        print('0.000')
    else:
        arr = input().split()
        set_heights = set_maker(arr, N)
        result = average(set_heights)
        print(result)
