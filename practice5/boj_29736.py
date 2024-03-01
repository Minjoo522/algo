"""
본인과 푼 문제 수 차이가 X보다 작거나 같은 사람만 친구의 자격을 갖추었다
브실이의 친구가 될 수 있는 사람의 수
"""
import sys

input = sys.stdin.readline

A, B = map(int, input().split())
K, X = map(int, input().split())

people = [i for i in range(A, B + 1)]
ans = 0

for p in people:
    if abs(K - p) <= X:
        ans += 1

if ans == 0:
    print("IMPOSSIBLE")
else:
    print(ans)
