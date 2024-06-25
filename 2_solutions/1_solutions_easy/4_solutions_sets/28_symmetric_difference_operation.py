#!/usr/bin/python3

def symmetric_difference(n: int, eng_np: set, m: int, fre_np: set) -> int:
    sd = eng_np.symmetric_difference(fre_np)
    return sd

if __name__=='__main__':
    n = int(input())
    eng_np = set(map(int, input().split()))
    m = int(input())
    fre_np = set(map(int, input().split()))
    print(len(symmetric_difference(n, eng_np, m, fre_np)))