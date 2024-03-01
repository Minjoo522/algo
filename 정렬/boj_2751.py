# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# arr = [int(input()) for _ in range(N)]
# arr.sort()
#
# for a in arr:
#     print(a)
import sys

input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]


def merge_sort(input_list):
    if len(input_list) == 1:
        return input_list

    mid = len(input_list) // 2
    left_half = input_list[:mid]
    right_half = input_list[mid:]

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def merge(left, right):
    result = [0] * (len(left) + len(right))
    l = r = idx = 0  # 포인터

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result[idx] = left[l]
            l += 1
            idx += 1
        else:
            result[idx] = right[r]
            r += 1
            idx += 1
    while l < len(left):
        result[idx] = left[l]
        l += 1
        idx += 1
    while r < len(right):
        result[idx] = right[r]
        r += 1
        idx += 1

    return result


print(*merge_sort(arr))
