import sys

input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))
high_score = max(scores)

fixed_scores = [score / high_score * 100 for score in scores]

print(sum(fixed_scores) / N)
