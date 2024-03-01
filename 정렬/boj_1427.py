import sys

input = sys.stdin.readline

N = input().rstrip()
arr = [num for num in N]
arr.sort(reverse=True)

print(''.join(map(str, arr)))

# 걍 이것도 됨
# nums = list(input())
# nums.sort(reverse=True)
#
# print(''.join(nums))
