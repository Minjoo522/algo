"""
M 이상 N 이하의 자연수 중
소수인 것을 골라
소수의 합, 최솟값
M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력
"""
import sys

input = sys.stdin.readline

M = int(input())
N = int(input())

primes = []
for i in range(M, N + 1):
    if i < 2:
        continue
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))
