# 5 4
# 2 1 2 4 4 3 4 5
V, E = map(int, input().split())
edges = list(map(int, input().split()))

# 트리 구조화
left = [0] * (V + 1)  # 왼쪽 자식 모아둠
right = [0] * (V + 1)  # 오른쪽 자식 모아둠
ancestors = [0] * (V + 1)  # 부모가 어떤 노드인지 모아둠

for i in range(E):
    parent, child = edges[i * 2], edges[i * 2 + 1]  # 부모는 짝수번째 인덱스에 있고, 자식은 홀수번째 인덱스에 있음
    if not left[parent]:
        left[parent] = child
    else:
        right[parent] = child
    ancestors[child] = parent

root = None
for j in range(1, V + 1):
    if ancestors[j] == 0:
        root = j
        break

# 순회
# print 위치만 다름


# 전위 순회 : 2, 1, 4, 3, 5
def preorder(node):
    if node > 0:
        print(node, end=' ')
        preorder(left[node])
        preorder(right[node])


# 중위 순회 : 1, 2, 3, 4, 5
def inorder(node):
    if node > 0:
        inorder(left[node])
        print(node, end=' ')
        inorder(right[node])


# 후위 순회 : 1, 3, 5, 4, 2
def postorder(node):
    if node > 0:
        postorder(left[node])
        postorder(right[node])
        print(node, end=' ')


preorder(root)
print()
inorder(root)
print()
postorder(root)