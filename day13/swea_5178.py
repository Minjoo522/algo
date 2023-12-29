"""
완전 이진트리
"""

for tc in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    CBT = [0] * (N + 1)  # Complete Binary Tree

    for _ in range(M):
        node, label = map(int, input().split())
        CBT[node] = label

    for i in range(N, L*2-1, -1):  # 노드의 제일 끝부터 차례 차례 더하기
        # L의 자식 노드는 L * 2, L * 2 + 1 두 개
        # 아래서부터 순서대로 가면 N 부터 L * 2번째 까지만 하면 됨(L * 2 + 1은 L * 2보다 큰 숫자니까 L * 2까지만 하면 포함됨)
        # range 두 번째 파라미터에서 해당 숫자는 포함이 안되므로 하나를 빼 주어야 함
        CBT[i//2] += CBT[i]

    print(f'#{tc} {CBT[L]}')
