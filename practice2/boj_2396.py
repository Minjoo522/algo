"""
팔방탐색(?)
1. x 표시된 곳이면(눌린 곳), directions들을 돌며 *이 몇 개인지 센다
2. 해당 자리에 넣어 줌
3. 만약에 해당 칸이 지뢰가 발견되었다면 '지뢰가 있는' 모든 칸을 *로 만들어준다
"""
import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, 1, -1, -1, 1, -1, 1]

N = int(input())

board = [input().rstrip() for _ in range(N)]
user = [input().rstrip() for _ in range(N)]

ans = [['.'] * N for _ in range(N)]
found = False

for r in range(N):
    for c in range(N):
        if user[r][c] == 'x':
            cnt = 0
            for d in range(8):
                nr, nc = r + dr[d], c + dc[d]

                if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == '*':
                    cnt += 1
            ans[r][c] = str(cnt)  # join 하기 위해서 string으로 저장해주어야 함

            if board[r][c] == '*':
                found = True

if found:
    for r in range(N):
        for c in range(N):
            if board[r][c] == '*':
                ans[r][c] = '*'

for line in ans:
    print(''.join(line))
