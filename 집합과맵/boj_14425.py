import sys

input = sys.stdin.readline

N, M = map(int, input().split())

word_sets = set(input().rstrip() for _ in range(N))
words = list(input().rstrip() for _ in range(M))

ans = 0
for word in words:
    if word in word_sets:
        ans += 1

print(ans)