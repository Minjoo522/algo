"""
<자료구조 모양>
1. 2차원 리스트 => N * N

<로직>
1. 2차원 리스트 순회
2. M * M 의 2차원 리스트 돌면서 모든 숫자 더하기
3. 최대값 갱신
"""

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0

    for r in range(N - M + 1):
        for c in range(N - M + 1):
            tmp = 0
            for i in range(r, r + M):
                for j in range(c, c + M):
                    tmp += board[i][j]
            max_val = max(max_val, tmp)

    print(f'#{tc} {max_val}')
