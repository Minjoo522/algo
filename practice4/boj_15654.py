"""
N개의 수중에
길이가 M인 수열
순열
"""
import sys

input = sys.stdin.readline


def perm(depth):
    if depth == M:
        print(*ans)
        return

    for i in range(N):
        if not check[i]:
            check[i] = 1
            ans[depth] = nums[i]
            perm(depth + 1)
            check[i] = 0


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
check = [0] * N
ans = [0] * M

perm(0)
