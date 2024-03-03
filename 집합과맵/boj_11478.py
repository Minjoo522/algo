import sys

input = sys.stdin.readline

S = input().rstrip()

result = []

length = len(S)

for start in range(length):
    for end in range(start + 1, length + 1):
        result.append(S[start:end])

print(len(set(result)))
