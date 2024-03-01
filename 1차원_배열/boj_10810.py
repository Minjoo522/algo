import sys

input = sys.stdin.readline

N, M = map(int, input().split())
basket = [0 for _ in range(N + 1)]

for _ in range(M):
    first, last, ball_num = map(int, input().split())
    for i in range(first, last + 1):
        basket[i] = ball_num

print(*basket[1:])
