import sys
input = sys.stdin.readline

student = [int(input()) for _ in range(28)]
incomplete_homework_student = [i for i in range(1, 31) if i not in student]

sorted(incomplete_homework_student)

for s in incomplete_homework_student:
    print(s)