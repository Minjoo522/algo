"""
평균과 중간 값
"""
import sys

input = sys.stdin.readline

nums = [int(input()) for _ in range(5)]

print(sum(nums) // 5)

for i in range(len(nums) - 1):
    min_idx = i

    for j in range(i + 1, len(nums)):
        if nums[j] < nums[min_idx]:
            min_idx = j

    nums[i], nums[min_idx] = nums[min_idx], nums[i]

print(nums[2])
