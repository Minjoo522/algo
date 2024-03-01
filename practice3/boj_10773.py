"""
잘못된 수를 불렀으면 0 -> 최근에 쓴 숫자를 지운다 => pop()
모든 수를 받아 적고 그 수의 합
"""
import sys
input = sys.stdin.readline
nums = []

for _ in range(int(input())):
    num = int(input())
    if num == 0:
        nums.pop()
        continue
    nums.append(num)

print(sum(nums))

# deque로 풀기
# from collections import deque
#
# stack = deque()
#
# for _ in range(int(input())):
#     num = int(input())
#
#     if num == 0:
#         stack.pop()
#         continue
#     stack.append(num)
#
# print(sum(stack))