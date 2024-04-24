#!/usr/bin/python3

def union(n: int, eng_np: set, m:int, fre_np: set) -> int:
    u = eng_np.union(fre_np)
    return u


if __name__ == '__main__':
    n = int(input())
    eng_np = set(map(int,input().split()))
    m = int(input())
    fre_np = set(map(int,input().split()))
    print(len(union(n, eng_np, m, fre_np)))
