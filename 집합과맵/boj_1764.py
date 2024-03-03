import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nosee = set()
nowathch = set()

for i in range(1, N + M + 1):
    if i <= N:
        nosee.add(input().rstrip())
    else:
        nowathch.add(input().rstrip())

noseewatch = nosee.intersection(nowathch)
result = sorted(noseewatch)

print(len(result))
print(*result)
