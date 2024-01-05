"""
오른쪽에만 자녀가 있는 경우도 존재하는 문제

딕셔너리 구조화
for _ in range(V):
    parent, L, R = input().split()
    tree[parent] = [L, R]

* 전위 순회
DFS : 탐색 즉시 방문(방문 즉시 print)

* 중위 / 후위 순회 - 탐색과 방문이 분리

* 중위 순회
"왼쪽" 서브 트리가 "없거나" 모두 방문한 경우에만 방문
오른쪽에 서브 트리가 있어도 왼쪽에 없으면 바로 방문!

* 후위 순회
서브 트리가 없거나 모두 방문한 경우에만 방문
"""


# 전위 순회
def preorder(now):
    print(now, end='')  # 루트
    if tree[now][0] != '.':  # 왼쪽 자식
        preorder(tree[now][0])
    if tree[now][1] != '.':
        preorder(tree[now][1])


# 중위 순회
def inorder(now):
    if tree[now][0] != '.':
        inorder(tree[now][0])
    # 왼쪽 트리 다 ~ 찍고 print
    print(now, end='')
    if tree[now][1] != '.':
        inorder(tree[now][1])


# 후위 순회
def postorder(now):
    if tree[now][0] != '.':
        postorder(tree[now][0])
    if tree[now][1] != '.':
        postorder(tree[now][1])
    print(now, end='')


V = int(input())
tree = dict()

for _ in range(V):
    parent, L, R = input().split()
    tree[parent] = [L, R]
