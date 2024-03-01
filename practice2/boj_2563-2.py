"""
가로, 세로가 각 100 / 색종이 10
색종이가 붙은 영역의 넓이 구하기
1. 색종이의 수
2. 색종이를 붙인 위치 ...
    색종이 왼쪽 변과 오른쪽 변의 거리 - 색종이 아래쪽과 도화지 아래쪽 변의 거리

데이터 타입 : 이차원 리스트
"""
import sys
input = sys.stdin.readline

board = [[0] * 100 for _ in range(100)]

for _ in range(int(input())):
    X, Y = map(int, input().split())

    for x in range(X, X + 10):
        for y in range(Y, Y + 10):
            board[x][y] = 1

ans = sum(sum(line) for line in board)
print(ans)
