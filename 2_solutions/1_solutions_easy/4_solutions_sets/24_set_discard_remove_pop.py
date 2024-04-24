#!/bin/python

def process(n: int , N: int, s: set) -> int:
    result = 0
    for i in range(N):
        method_value = input().split()
        method = method_value[0]
        if len(method_value) == 2:
            value = int(method_value[1])
            if method == 'discard':
                s.discard(value)
            else:
                s.remove(value)
        elif method == 'pop':
            s.pop()

    for j in s:
        result += j
    
    return result

if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())
    print(process(n, N, s))