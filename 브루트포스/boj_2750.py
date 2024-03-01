"""
오름차순
"""
import sys

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

for i in range(N - 1, 0, -1):
    for j in range(i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

for num in nums:
    print(num)
