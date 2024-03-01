import sys

input = sys.stdin.readline

subject_grades = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

major_score = 0
total_score = 0

for _ in range(20):
    subject, score, grade = input().split()
    score = float(score)
    if grade == "P":
        continue
    major_score += score * subject_grades[grade.rstrip()]
    total_score += score

print(major_score / total_score)
