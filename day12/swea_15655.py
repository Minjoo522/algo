def combination(idx, depth):
    if depth == M:
        print(*ans)
        return

    for i in range(idx, N):
        if i not in visited:
            visited.add(i)
            ans.append(nums[i])
            combination(i + 1, depth + 1)
            ans.pop()
            visited.discard(i)


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = set()
ans = []

combination(0, 0)
