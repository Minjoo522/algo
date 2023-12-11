"""
<자료구조 모양>
1. 2차원 리스트 => N * M

<로직>
1. 시작 : (0, 0)
2. 터뜨린 풍선 위치 숫자 + 범위 내에 있는 상, 하, 좌, 우
    2.1 범위 : r - 0보다 크거나 같고 N보다 작음
            c - 0보다 크거나 같고 M보다 작음
3. 모든 위치의 풍선 다 터뜨리며 max 값 갱신
"""

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0

    for r in range(N):
        for c in range(M):
            tmp = board[r][c]

            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]

                if 0 <= nr < N and 0 <= nc < M:
                    tmp += board[nr][nc]

            max_val = max(max_val, tmp)

    print(f'#{tc} {max_val}')
