import sys
from collections import deque

input = sys.stdin.readline

K = int(input())
moneys = deque()

for _ in range(K):
    command = int(input())
    if command == 0:
        moneys.pop()
    else:
        moneys.append(command)

print(sum(moneys))
