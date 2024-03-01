import sys

input = sys.stdin.readline

nums = list(input().split())
sangsoo_nums = [int(num[::-1]) for num in nums]
print(max(sangsoo_nums))
