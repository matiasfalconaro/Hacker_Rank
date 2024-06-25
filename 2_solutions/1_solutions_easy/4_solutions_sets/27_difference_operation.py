#!/usr/bin/python3

def difference(n: int, eng_np: set, m: int, fre_np: set) -> int:
    d = eng_np.difference(fre_np)
    return d


if __name__=='__main__':
    n = int(input())
    eng_np = set(map(int, input().split()))
    m = int(input())
    fre_np = set(map(int, input().split()))
    print(len(difference(n, eng_np, m, fre_np)))