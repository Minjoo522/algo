import sys

input = sys.stdin.readline

N, K = map(int, input().split())
scores = list(map(int, input().split()))

indexed_scores = list(enumerate(scores))
sorted_scores = sorted(indexed_scores, key=lambda x: x[1], reverse=True)
selected = [sorted_scores[i][0] for i in range(K)]

ans = 0
current_student = K
for i in range(max(selected) + 1):
    ans += scores[i] * current_student
    if i in selected:
        current_student -= 1

print(ans)
