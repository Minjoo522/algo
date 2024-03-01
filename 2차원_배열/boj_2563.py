import sys

input = sys.stdin.readline

board = [[0] * 100 for _ in range(100)]

N = int(input())

for _ in range(N):
    X, Y = map(int, input().split())
    for x in range(X, X + 10):
        for y in range(Y, Y + 10):
            board[y][x] = 1

result = sum(sum(line) for line in board)
print(result)
