#!usr/bin/python3

def intersection(n: int, eng_np: set, m: int, fre_np: set) -> int:
    i = eng_np.intersection(fre_np)
    return i


if __name__ == '__main__':
    n = int(input())
    eng_np = set(map(int, input().split()))
    m = int(input())
    fre_np = set(map(int, input().split()))
    print(len(intersection(n, eng_np, m, fre_np)))