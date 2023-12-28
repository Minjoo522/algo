# 임의의 위치에서 시작
# 시작 위치로 되돌아 갈 것

def dfs(now, cost, depth):
    global ans

    if depth == N:  # 시작점으로 돌아갈 수 있으면 정답 갱신
        if cost_matrix[now][0]:
            cost += cost_matrix[now][0]
            ans = min(ans, cost)
            return
    else:  # 길이 없다면 더 이상 탐색하면 안됨
        return

    # 백트래킹
    if cost > ans:
        return

    for after in range(N):
        if not visited[after] and cost_matrix[now][after]:
            visited[after] = 1
            dfs(after, cost + cost_matrix[now][after], depth + 1)
            visited[after] = 0


N = int(input())
cost_matrix = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * N
ans = 987654321

visited[0] = 1
dfs(0, 0, 1)  # 진짜 dfs의 시작은 1번 depth부터

print(ans)
