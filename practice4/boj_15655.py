"""
길이가 M인 수열
오름차순
중복 안됨
순서 중요하지 않음 => 조합
"""
import sys

input = sys.stdin.readline


def combination(idx, sidx):
    if sidx == M:
        print(*ans)
        return

    if idx == N:
        return

    ans[sidx] = nums[idx]
    combination(idx + 1, sidx + 1)
    combination(idx + 1, sidx)


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = [0] * M

combination(0, 0)


# 순열과 비슷한 버전
"""
import sys
input = sys.stdin.readline

def combination(depth, idx):

    if depth == M:
        print(*ans)
        return

    for i in range(idx, N):
        if not check[i]:
            check[i] = 1
            ans[depth] = nums[i]
            combination(depth + 1, i + 1)
            check[i] = 0

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

check = [0] * N
ans = [0] * M

combination(0, 0)
"""