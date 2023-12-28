def perm(depth):
    if depth == M:
        print(*ans)
        return

    for num in nums:
        if num not in visited:
            visited.add(num)
            ans.append(num)
            perm(depth + 1)
            ans.pop()
            visited.discard(num)


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = set()
ans = []

perm(0)
