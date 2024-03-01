# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# arr = list(map(int, input().split()))
# nums = [0] * N
#
# arr_index = [(index, value) for index, value in enumerate(arr)]
#
# arr_index.sort(key=lambda x: x[1])
#
# nums[arr_index[0][0]] = 0
#
# current_idx = 0
# for i in range(1, N):
#     if arr_index[i][1] != arr_index[i - 1][1]:
#         current_idx += 1
#     nums[arr_index[i][0]] = current_idx
#
# print(*nums)

# arr = list(map(int, stdin.read().split()))
# dic = {x: i for i, x in enumerate(sorted(set(arr)))}
# print(' '.join(map(str, [dic[x] for x in arr])))
import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
dic = {x: i for i, x in enumerate(sorted(set(arr)))}
ans = [dic[x] for x in arr]

print(*ans)
