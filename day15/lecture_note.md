# 트리의 부모 찾기
- 루트 없는 트리 : 그래프
- 연결된 두 정점 : 간선
- 무방향 그래프, 양방향 그래프로 구조화
- 트리의 간선은 언제나 N-1
- DFS/BFS로 순회
- 완전 탐색 : DFS == BFS

# 트리 순회
### 트리 딕셔너리로 구조화
~~~python
for _ in range(V):
    parent, L, R = input().split()
    tree[parent] = [L, R]
~~~

### 전위 순회
- DFS : 탐색 즉시 방문(방문 즉시 print)

> 중위 / 후위 순회 - 탐색과 방문이 분리

### 중위 순회
- "왼쪽" 서브 트리가 "없거나" 모두 방문한 경우에만 방문
- 오른쪽에 서브 트리가 있어도 왼쪽에 없으면 바로 방문!

### 후위 순회
- 서브 트리가 없거나 모두 방문한 경우에만 방문