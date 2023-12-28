"""
이전 방문지에 숫자 +1 하면서 돌면 마지막 지점의 숫자가 최종 방문 갯수가 됨
"""

from collections import deque

dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
Q = deque([(0, 0)])  # list 안에 튜플을 넣어주어야 함

while Q:
    r, c = Q.popleft()

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        # 1인 곳으로만 이동 가능하므로
        if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == 1:
            maze[nr][nc] = maze[r][c] + 1
            Q.append((nr, nc))

print(maze[N - 1][M - 1])
