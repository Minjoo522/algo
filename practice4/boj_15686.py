"""
조합
from itertools import combinations

arr = ['A', 'B', 'C']
for x, y in combinations(arr, 2):  # 3C2
    print(x, y)
"""
import sys
input = sys.stdin.readline

from itertools import combinations

N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            house.append((r, c))
        elif city[r][c] == 2:
            chicken.append((r, c))

ans = 987654321

for case in combinations(chicken, M):
    cnt = 0
    for h in house:
        tmp = 987654321
        for store in case:
            tmp = min(tmp, abs(store[0] - h[0]) + abs(store[1] - h[1]))
        cnt += tmp

        if cnt > ans:
            break

    ans = min(ans, cnt)

print(ans)