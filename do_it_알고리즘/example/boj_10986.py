import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m  # 업데이트 된 합 배열 중 동일한 값을 가진 애들이 몇 개 인지
answer = 0

S[0] = A[0]
for i in range(1, n):
    S[i] = S[i - 1] + A[i]

for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        answer += 1
    C[remainder] += 1

for i in range(m):
    if C[i] > 1:  # 같은 나머지 값을 갖는 애가 2개 이상 있으면
        answer += C[i] * (C[i] - 1) // 2  # combination 공식(무조건 2개 뽑음)

print(answer)
