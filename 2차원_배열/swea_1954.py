dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

for tc in range(1, int(input()) + 1):
    N = int(input())

    snail = [[0] * N for _ in range(N)]
    r, c, d = 0, 0, 0

    for num in range(1, N ** 2 + 1):
        snail[r][c] = num

        # 기존 방향
        nr, nc = r + dr[d], c + dc[d]

        if nr < 0 or nr >= N or nc < 0 or nc >= N or snail[nr][nc] != 0:
            d = (d + 1) % 4
            nr, nc = r + dr[d], c + dc[d]

        r, c = nr, nc

    print(f"#{tc}")
    for s in snail:
        print(*s)
