#!/bin/python3

from typing import List, Any

def create_students(n: int) -> List[List[Any]]:
    "Given the names and grades for each student creates nested lists in a list"
    if 2 <= n <= 5:
        records = []
        for _ in range(n):
            name = input()
            score = float(input())
            records.append([name, score])
        return records
    else:
        print('The input should be an integer between 2 and 5')

def check_grade(records: List[List[Any]]) -> List[str]:
    "Given a nested list of lists finds the second lowest grade"
    scores = []
    for record in records:
        scores.append(record[1])
    scores.sort()

    second_lowest_grade = None
    for score in scores:
        if score > scores[0]:
            second_lowest_grade = score
            break

    students_with_second_lowest_grade = []
    for name, score in records:
        if score == second_lowest_grade:
            students_with_second_lowest_grade.append(name)

    students_with_second_lowest_grade.sort()

    return students_with_second_lowest_grade

if __name__ == '__main__':
    n = int(input())
    records = create_students(n)
    students_with_second_lowest_grade = check_grade(records)
    for student in students_with_second_lowest_grade:
        print(student)