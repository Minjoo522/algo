"""
킹, 퀸, 룩, 비숍, 나이트, 폰
1, 1, 2, 2, 2, 8
"""
import sys

input = sys.stdin.readline

chess = [1, 1, 2, 2, 2, 8]
donghyeok_chess = list(map(int, input().split()))

# 방법 1
# result = [0 for _ in range(len(chess))]
#
# for i in range(len(chess)):
#     result[i] = chess[i] - donghyeok_chess[i]
#
# print(*result)

# 방법 2
result = list(map(lambda x, y: x - y, chess, donghyeok_chess))

print(*result)
