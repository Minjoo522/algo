"""
1. 100 * 100의 빈 도화지(이차원 리스트)를 만든다
2. x(왼쪽), y(위쪽) 숫자로부터 시작해 10만큼 순회하며 1을 더해준다
3. 모든 숫자를 더한다
"""
import sys
input = sys.stdin.readline

board = [[0] * 100 for _ in range(100)]

for _ in range(int(input())):
    X, Y = map(int, input().split())

    for x in range(X, X + 10):
        for y in range(Y, Y + 10):
            board[y][x] = 1  # 겹치는 부분도 1

print(sum(sum(line) for line in board))
