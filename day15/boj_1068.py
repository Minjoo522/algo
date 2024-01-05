"""
노드를 지울 때 노드의 모든 자손이 다 지워짐
루트 노드 : -1

지울 노드의 번호를 K라 할 때, K를 정점으로 하는 서브 트리를 모두 지우기
정점을 시작으로 DFS / BFS 돌면 모든 subtree를 지울 수 있음
- 방문 표시를 어떻게 할지? : -1로 표시

리프 노드의 특징
- 부모 노드를 나타내는 리스트에 자기 자신이 없음
- i로 돌면서 자기 자신이 없으면서 -1이 아닐 때 개수 +
"""
import sys

input = sys.stdin.readline


def dfs(now):
    tree[now] = -2

    for after in range(N):
        if tree[after] == now:
            dfs(after)


N = int(input())
tree = list(map(int, input().split()))
K = int(input())

dfs(K)
cnt = 0

for i in range(N):
    if tree[i] != -2 and i not in tree:
        cnt += 1

print(cnt)
