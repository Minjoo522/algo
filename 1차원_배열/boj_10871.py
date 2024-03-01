import sys

input = sys.stdin.readline

N, X = map(int, input().split())
nums = list(map(int, input().split()))

result = [num for num in nums if num < X]
print(*result)
