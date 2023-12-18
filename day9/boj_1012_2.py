import sys

input = sys.stdin.readline

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def BFS(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if (nx, ny) in cabbages:
                queue.append((nx, ny))
                cabbages.discard((nx, ny))


for _ in range(int(input())):
    M, N, K = map(int, input().split())
    cabbages = set(tuple(map(int, input().split())) for _ in range(K))
    ans = 0

    while cabbages:
        i, j = cabbages.pop()
        BFS(i, j)
        ans += 1

    print(ans)
