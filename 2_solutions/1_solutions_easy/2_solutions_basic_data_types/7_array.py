#!/bin/python3

from typing import List


def sort_array(arr: List[int]) -> int:
    """
    Find the score of the runner-up from a list of scores.
    """
    sorted_arr = sorted(set(arr))

    if len(sorted_arr) >= 2:
        runner_up = sorted_arr[-2]
    else:
        runner_up = sorted_arr[0]
    return runner_up


if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))

    if len(scores) != n:
        print(f"Please enter exactly {n} scores.")
    else:
        print(sort_array(scores))
