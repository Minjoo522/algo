"""
내 풀이
for tc in range(1, int(input()) + 1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))

    left = [0] * (E + 1 + 1)
    right = [0] * (E + 1 + 1)
    ancestors = [0] * (E + 1 + 1)

    for i in range(E):
        parent, child = edges[i * 2], edges[i * 2 + 1]
        if not left[parent]:
            left[parent] = child
        else:
            right[parent] = child
        ancestors[child] = parent

    nodes = []


    def preorder(node):
        if node > 0:
            nodes.append(node)
            preorder(left[node])
            preorder(right[node])


    preorder(N)
    print(f'#{tc} {len(nodes)}')
"""

T = int(input())


def preorder(v):
    global cnt
    cnt += 1  # 들어오자마자 하나 추가
    if left[v] > 0:  # 있을때만 가라
        preorder(left[v])
    if right[v] > 0:
        preorder(right[v])


for tc in range(1, T+1):
    E, N = map(int, input().split())  # E 간선갯수, N 시작점
    edges = list(map(int, input().split()))
    left = [0]*(E+2)  # 왼쪽 자식
    right = [0]*(E+2)  # 오른쪽 자식
    cnt = 0

    for i in range(E):
        parent, child = edges[2*i], edges[2*i+1]  # 채우기
        if not left[parent]:  # 왼쪽 자식 없으면 왼쪽부터 추가
            left[parent] = child
        else:
            right[parent] = child

    preorder(N)

    print('#{} {}'.format(tc, cnt))
