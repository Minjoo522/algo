import sys

input = sys.stdin.readline

N = int(input())

factors = []

while N % 2 == 0:
    factors.append(2)
    N = N // 2

for i in range(3, int(N ** 0.5) + 1, 2):  # 홀수 소수들에 대해 검사(짝수는 소수가 될 수 없음 - 2로 나누어짐)
    while N % i == 0:
        factors.append(i)
        N = N // i

# N이 소수인 경우
if N > 2:
    factors.append(N)

sorted(factors)

for factor in factors:
    print(factor)
