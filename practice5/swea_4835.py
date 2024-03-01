for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    sums = []

    for i in range(N-M+1):
        target = nums[i:i+M]
        sums.append(sum(target))

    print(f'#{tc} {max(sums) - min(sums)}')