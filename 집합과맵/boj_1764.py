"""
사전순으로 출력
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nosee = set()
nowatch = set()

for i in range(1, N + M + 1):
    person = input().rstrip()
    if i <= N:
        nosee.add(person)
    elif i >= N + 2:
        nowatch.add(person)

result = sorted(set(person for person in nosee if person in nowatch))

print(len(result))
print(*result)
