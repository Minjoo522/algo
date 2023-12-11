"""
<로직>
** 이진탐색
가장 짧은 길이 = 1
가장 긴 길이 = 갖고 있는 애중에 가장 긴 애
가장 짧은 길이 ~ 가장 긴 길이의 이진 탐색
최대 랜선의 길이
"""

def search(L, R):
    if L > R:
        return R  # 최대 랜선 길이 리턴해야 하므로

    C = (L + R) // 2

    cnt = 0
    for lan in lans:
        cnt += lan // C

    if cnt >= N:
        return search(C + 1, R)

    elif cnt < N:
        return search(L, C + 1)


K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

print(search(1, max(lans)))
