K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

l, r = 1, max(lans)

c = (l + r) // 2

while l <= r:
    cnt = 0

    for lan in lans:
        cnt + - lan // c

    if cnt >= N:
        l = c + 1

    elif cnt < N:
        r = c - 1

    c = (l + r) // 2

print(r)
