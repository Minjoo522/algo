from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def bfs(r, c):
    queue = deque([(r, c)])
    ground[r][c] = 0

    while queue:
        r, c = queue.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and ground[nr][nc] != 0:
                ground[nr][nc] = 0
                queue.append((nr, nc))


for _ in range(int(input())):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]
    ans = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        ground[Y][X] = 1

    for r in range(N):
        for c in range(M):
            if ground[r][c] == 1:
                ans += 1
                bfs(r, c)

    print(ans)
