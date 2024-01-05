"""
길을 유지하는데 드는 유지비 : 간선 가중치
모든 집을 연결 + 유지비의 합을 최소화 = 최소신장트리!
MST에서 가장 비용이 큰 간선을 자른다

1. 크루스칼 알고리즘
- 간선 가중치순 정렬
- parents 보조 리스트 필요 : 싸이클 없애기(싸이클이 있다 != 최소신장트리)
- 부모를 타고 올라가서 부모가 동일하다면 연결할 수 없음 => 연결시 싸이클이 생기니까
- 간선 추가해도 싸이클 안 만들어지면 연결
- 트리의 특징 : 정점이 N개일 때 간선의 개수가 N - 1개 간선이 N - 1개가 됐다면 더이상 확인 x
- 항상 마지막에 뽑은 간선이 최대 가중치

2. 프림 알고리즘
- 정점을 기준으로 MST를 만듦
- 인접 리스트 구조화 + 임의의 정점에서 시작
- 1. 인덱스 : [(가중치, 정점) ...]
- 2. 해당 정점을 선택할 때 해당 정점으로 들어가는 가중치가 갱신될 표
- 3. heap(가장 작은 숫자가 제일 앞으로 오는 걸 보장하는 자료구조) : 1부터 시작
- heap pop
- 가중치 갱신
- 갈 수 있는 모든 애들을 heap에 넣음(가능성이 있는 애들, 아직 방문 안한 애들)
- 모든 정점을 방문할 때까지
- 최대 간선이 언제 뽑힐지 모름

* 크루스칼이 더 적합
"""


# # 조상 찾기
# def find_set(x):
#     if p[x] != x:
#         p[x] = find_set(p[x])
#     return p[x]
#
#
# # 이어주기
# def union(x, y):
#     p[find_set(y)] = find_set(x)
#
#
# V, E = map(int, input().split())
# edges = [tuple(map(int, input().split())) for _ in range(E)]
# edges.sort(key=lambda x: x[2])
#
# p = [i for i in range(V + 1)]
#
# dist = 0
# max_dist = 0
# cnt = 0
#
# for x, y, w in edges:
#     if find_set(x) != find_set(y):  # 채택됨
#         union(x, y)
#         dist += w
#         cnt += 1
#
#         if cnt == V - 1:
#             dist -= w
#             break
#
# print(dist)

import heapq

V, E = map(int, input().split())

adj = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    adj[s].append((w, e))
    adj[e].append((w, s))

dist = [987654321] * (V + 1)  # 가중치 갱신될 리스트
visited = set()
heap = []

dist[0] = 0  # 0은 사용하지 않음
dist[1] = 1
heapq.heappush(heap, (0, 1))  # 1부터 시작, 1은 가중치가 없으므로 0

while heap:
    wei, now = heapq.heappop(heap)

    if now in visited:
        continue

    dist[now] = wei
    visited.add(now)

    if len(visited) == V:
        break

    for next_wei, next_node in adj[now]:
        if next_node not in visited and next_wei < dist[next_node]:
            heapq.heappush(heap, (next_wei, next_node))

ans = sum(dist) - max(dist)

print(ans)