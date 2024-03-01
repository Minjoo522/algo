import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

cnt = 0
for num in nums:
    if num < 2:
        continue
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  # int(num ** 0.5) : 제곱근 구하기
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        cnt += 1

print(cnt)
