import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
persons = defaultdict(str)

for _ in range(N):
    p, c = input().rstrip().split()

    persons[p] = c

enters = []

for key, value in persons.items():
    if value == "enter":
        enters.append(key)

enters.sort(reverse=True)

print(*enters)
