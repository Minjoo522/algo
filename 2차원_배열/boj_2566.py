import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]

# 방법 1
# max_value = 0
# max_index = [0, 0]
#
# for x in range(9):
#     for y in range(9):
#         if board[x][y] >= max_value:
#             max_value = board[x][y]
#             max_index[0], max_index[1] = x + 1, y + 1

# 방법 2
max_value = max(max(row) for row in board)
max_index = [(x + 1, y + 1) for x, row in enumerate(board) for y, value in enumerate(row) if value == max_value][0]

print(max_value)
print(*max_index)
