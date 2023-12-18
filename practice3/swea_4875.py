"""
출발지 : 2 / 목적지 : 3

경로 존재 확인 문제
DFS
"""

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for tc in range(1, int(input()) + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    stack = []
    ans = 0

    for r in range(N):
        for c in range(N):
                stack.append((r, c))
                break
        if stack:
            break

    while stack:
        r, c = stack.pop()

        if maze[r][c] == 3:
            ans = 1
            break

        maze[r][c] = 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1:
                stack.append((nr, nc))

    print(f'#{tc} {ans}')