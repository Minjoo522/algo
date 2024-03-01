import sys

input = sys.stdin.readline

N, M = map(int, input().split())

baskets = [i for i in range(N + 1)]

for _ in range(M):
    b1, b2 = map(int, input().split())
    baskets[b1:b2 + 1] = baskets[b2:b1 - 1:-1]

print(*baskets[1:])
