import sys
input = sys.stdin.readline

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(r, c, num):
    stack = deque([(r, c, num)])

    while stack:
        r, c, num = stack.pop()
        if len(num) == 6:
            cases.add(num)
            continue

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < 5 and 0 <= nc < 5:
                stack.append((nr, nc, num + board[nr][nc]))


board = [input().split() for _ in range(5)]  # string으로 저장(string + 연산자로 뒤에 이어지게)
cases = set()  # 중복된 결과는 자동으로 append 되지 않도록 set 이용

for r in range(5):
    for c in range(5):
        dfs(r, c, board[r][c])

print(len(cases))
