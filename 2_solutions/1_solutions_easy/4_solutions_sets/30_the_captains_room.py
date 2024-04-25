#!/usr/bin/python3

from typing import Dict, List


def count_rooms(count: Dict, s: List) -> Dict:
    for room in s:
        if room in count:
            count[room] += 1
        else:
            count[room] = 1
    return count


def find_room(K: int, S: set, rooms_count: Dict) -> int:
    for room in S:
        if rooms_count[room] != K:
            result = room
    return result


if __name__=='__main__':
    K = int(input())
    s = input().split()
    S = set(s)
    count = {}
    rooms_count = count_rooms(count, s)
    print(find_room(K, S, rooms_count))
    
