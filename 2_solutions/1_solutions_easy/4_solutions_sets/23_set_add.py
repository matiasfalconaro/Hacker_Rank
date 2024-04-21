#1/bin/python3

from typing import List

def get_countries(N: int, countries: str) -> List:
    for i in range(N):
        country = input()
        countries.append(country)
    return countries


if __name__ == "__main__":
    N = int(input())
    countries = []
    result = len(set(map(str, get_countries(N, countries))))
    print(result)