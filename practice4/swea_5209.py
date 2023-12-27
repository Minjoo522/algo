for tc in range(1, int(input()) + 1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    ans = 99999999999999
    check = [0] * N

    def perm(depth, acc):
        global ans

        if acc > ans:
            return

        if depth == N:
            ans = min(ans, acc)
            return

        for i in range(N):
            if not check[i]:
                check[i] = 1
                perm(depth + 1, acc + V[depth][i])
                check[i] = 0

    perm(0, 0)
    print(f'#{tc} {ans}')