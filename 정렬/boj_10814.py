import sys

input = sys.stdin.readline

N = int(input())
members = [tuple(input().rstrip().split()) for _ in range(N)]

members.sort(key=lambda x: int(x[0]))

for m in members:
    print(*m)
