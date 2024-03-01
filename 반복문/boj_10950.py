import sys

input = sys.stdin.readline

for _ in range(0, int(input())):
    A, B = map(int, input().split())
    print(f"{A + B}")
