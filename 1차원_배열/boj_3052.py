import sys

input = sys.stdin.readline

nums = [int(input()) % 42 for _ in range(10)]
unique_nums = list(set(nums))

print(len(unique_nums))
