"""
1. 빈 리스트 만들기
2. 큰 리스트 안에 갈 수 있는 정점들 넣은 양방향 그래프 리스트 -> 이차원 리스트
3. 탐색 => DFS or BFS
4. 노드가 적힐 정답 리스트 생성

<BFS>
1. queue(선입선출)에 첫 번째 항 push => (부모 정점, 현재 정점) => 지금 있는 부모 노드가 궁금하니까
2. 1은 부모 노드가 없기 때문에 가상의 부모 노드 0을 넣음 => [(0, 1)]
3. 방문지에 넣고 1 방문
4. 1에서 갈 수 있는 애들 queue에 넣음 => [(1, 4), (1, 6)]
...
5. 전부 다 탐색
"""
from collections import  deque

N = int(input())

adj = [[] for _ in range(N + 1)]

# 인접 리스트 생성
for _ in range(N - 1):
    s, e = map(int, input().split())

    adj[s].append(e)
    adj[e].append(s)

queue = deque([(0, 1)])
visited = {1}  # set
parents = [0] * (N + 1)

while queue:
    parent, child = queue.popleft()
    parents[child] = parent

    for n_child in adj[child]:
        if n_child not in visited:
            queue.append((child, n_child))
            visited.add(n_child)

for i in range(2, N + 1):
    print(parents[i])