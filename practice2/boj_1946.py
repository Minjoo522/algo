import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]

    arr.sort(key=lambda x: x[1])

    standard = N + 1
    ans = 0

    for i in range(N):
        if arr[i][0] < standard:
            ans += 1
            standard = arr[i][0]

    print(ans)
