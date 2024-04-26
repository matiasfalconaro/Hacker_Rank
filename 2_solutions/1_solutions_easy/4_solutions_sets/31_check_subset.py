#!usr/bin/python3


def is_subset(T: int) -> None:
    for i in range(T):
        N_A = int(input())
        A = set(map(int, input().split()))
        N_B = int(input())
        B = set(map(int, input().split()))
        result = A.intersection(B)
        if result == A:
            print('True')
        else:
            print('False')
    return None


if __name__=='__main__':
    T = int(input())
    is_subset(T)
