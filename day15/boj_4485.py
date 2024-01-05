"""
이차원 리스트 상에서 다익스트라

N * N 크기 동굴 : 이차원 리스트
일는 금액을 최소화 : 다익스트라
상하좌우 인접한 곳으로 1칸씩 이동 : 델타 탐색

정점마다 비용 == 간선 비용

1. 이차원 리스트
2. 가중치 이차원 리스트
3. heap
"""
from heapq import heappush, heappop

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dijstra(r, c):
    heap = []
    check[r][c] = 0
    heappush(heap, (arr[r][c], 0, 0))

    while heap:
        BR, r, c = heappop(heap)
        if r == N - 1 and c == N - 1:
            return BR
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                NBR = BR + arr[nr][nc]
                if check[nr][nc] > NBR:
                    check[nr][nc] = NBR
                    heappush(heap, (NBR, nr, nc))


tc = 0
while True:
    N = int(input())
    if N == 0:
        break

    tc += 1

    arr = [list(map(int, input().split())) for _ in range(N)]
    check = list([987654321] * N for _ in range(N))

    print(f'{"Problem"} {tc}: {dijstra(0, 0)}')
