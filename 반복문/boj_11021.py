import sys

input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    A, B = map(int, input().split())
    print(f"Case #{tc}: {A + B}")
