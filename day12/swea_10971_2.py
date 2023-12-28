# 방문 표시
# 방문 확인

def dfs(now, cost, depth, visited):
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
        if not cost_matrix[now][after] or visited & (1 << after):
            # 방문 확인
            # & 연산만 다름
            continue

        dfs(after, cost+cost_matrix[now][after], depth+1, visited | (1 << after))
        # 방문 표시
        # or 연산 특성상 이미 방문한 곳은 1, shift한 자리 수는 1로 바뀜


N = int(input())
cost_matrix = [list(map(int, input().split())) for _ in range(N)]

ans = 987654321

dfs(0, 0, 1, 1)

print(ans)
