"""
최단 거리
- 다익스트라 알고리즘

출발지, 도착지 : 유방향 그래프
1. 다익스트라 함수
    - 시작점으로부터 힙이 빌 때까지 거리 갱신
    - 항사 현재 최단 거리를 뽑아 갱신할 수 있으면 갱신
2. 간선 정보를 입력 받아 정점을 탐색할 수 있도록 인접 리스트/인접 행렬 구조화
    - 인접 행렬 : [x][y] = 가중치
    - 인접 리스트 : (가중치, 정점)
3. S, E를 받아서 1, 2를 사용해 정답 출력
- ✨최단 거리는 다른 최단 거리들의 합으로 이뤄져 있다

<자료 구조>
1. 인접 행렬
2. 가중치(✨출발점에서부터 거리의 합)
3. heap : 출발점부터 시작(0, 출발점)

<마지막으로 나오는 가중치>
시작점으로부터 해당 인덱스까지 걸리는 최단 거리
"""
from heapq import heappush, heappop


def dijkstra(start):
    visited = set()
    heap = []
    heappush(heap, (0, start))

    while heap:
        d, now = heappop(heap)

        if now not in visited:
            dist[now] = d
            visited.add(now)

            for after, tmp_d in dist_info[now]:
                if after in visited:
                    continue

                if dist[after] > d + tmp_d:  # 갱신 가능하다면
                    heappush(heap, (d + tmp_d, after))  # 출발지로부터의 거리


N = int(input())
M = int(input())

# 인접 리스트
dist_info = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    dist_info[s].append((e, c))

S, E = map(int, input().split())
dist = [987654321] * (N + 1)

dijkstra(5)
print(dist[E])
