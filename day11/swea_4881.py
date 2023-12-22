for tc in range(1, int(input()) + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    answer = 99999999999999
    check = [0] * N


    def perm(depth, acc):
        global answer

        # ✨ 중요
        if acc >= answer:
            return

        if depth == N:
            if answer > acc:
                answer = acc
            return

        for i in range(N):
            if not check[i]:
                check[i] = 1
                perm(depth + 1, acc + nums[depth][i])
                check[i] = 0


    perm(0, 0)

    print(f'#{tc} {answer}')
