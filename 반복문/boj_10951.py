import sys

input = sys.stdin.readline

while True:
    line = input()
    if not line:
        break
    A, B = map(int, line.split())
    print(A + B)
