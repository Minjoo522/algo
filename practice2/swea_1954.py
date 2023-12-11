"""
<자료구조 모양>
1. 2차원 리스트 => N * N
2. 0으로 초기화

<로직>
1. 달팽이는 시계 방향으로 돈다
2. 숫자는 1부터
3. 시작은 좌상단(0, 0)부터
4. 달팽이 방향 전환은?
    4.1 맵 밖으로 갈 것 같거나
    4.2 이미 숫자가 차있는 경우
5. 맵이 크면 클수록 방향을 0 1 2 3 0 1 2 3 이렇게 계속 바꾼다 => modular 연산
"""

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

for tc in range(1, int(input()) + 1):
    N = int(input())

    snail = [[0] * N for _ in range(N)]
    r, c, d = 0, 0, 0

    for num in range(1, N ** 2 + 1):
        snail[r][c] = num
        nr, nc = r + dr[d], c + dc[d]

        if nr < 0 or nr >= N or nc < 0 or nc >= N or snail[nr][nc] != 0:
            d = (d + 1) % 4
            nr, nc = r + dr[d], c + dc[d]

        r, c = nr, nc

    print(f'#{tc}')
    for ans in snail:
        print(*ans)
