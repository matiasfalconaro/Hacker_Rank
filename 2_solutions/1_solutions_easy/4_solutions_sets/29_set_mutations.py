#!/usr/bin/python3


def mutation_operations(n: int, A: set, N: int) -> set:
    for i in range(N):
        mutation = input().split()
        a = set(map(int, input().split()))
        if mutation[0] == 'intersection_update':
            A.intersection_update(a)
        elif mutation[0] == 'update':
            A.update(a)
        elif mutation[0] == 'symmetric_difference_update':
            A.simmetric_difference(a)
        else:
            A.difference_update(a)
    return A


if __name__=="__main__":
    n = int(input())
    A = set(map(int, input().split()))
    N = int(input())
    print(sum(mutation_operations(n, A, N)))