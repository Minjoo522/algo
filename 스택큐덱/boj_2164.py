import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
nums = deque(i for i in range(1, n + 1))

while len(nums) > 1:
    nums.popleft()
    tmp = nums.popleft()
    nums.append(tmp)

print(*nums)
