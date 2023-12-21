for tc in range(1, int(input()) + 1):
    N = int(input())
    nums = sorted(list(map(int, input().split())))

    ans = []

    for i in range(10):
        if i % 2 == 1:  # 홀수
            ans.append(nums.pop(0))

        elif i % 2 == 0:  # 짝수
            ans.append(nums.pop())

    print(f'#{tc}', end=' ')
    print(*ans)
