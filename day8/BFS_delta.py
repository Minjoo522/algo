from collections import deque  # pop(0) 대신 사용

dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]


def BFS(r, c):
    Q = deque()  # Q 처음 만들 때 deque() 객체 만듦
    Q.append((r, c))
    dist[r][c] = 1

    while Q:
        # curr_r, curr_c = Q.pop(0)  # 시간 초과 O(N)
        curr_r, curr_c = Q.popleft()

        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if arr[nr][nc] == 0 or dist[nr][nc] != 0:
                continue

            Q.append((nr, nc))
            dist[nr][nc] = dist[curr_r][curr_c] + 1


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
dist = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and dist[i][j] == 0:
            BFS(i, j)

for d in dist:
    print(*d)

# 결과
# 0 0 0 0 0 1 2
# 0 0 0 0 0 0 0
# 0 0 1 2 3 0 0
# 0 0 2 0 4 5 6
# 0 4 3 0 0 6 0
# 0 0 4 5 6 0 0
# 0 0 0 0 0 0 0
