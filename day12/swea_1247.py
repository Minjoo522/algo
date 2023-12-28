from collections import deque


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def dfs(now, distance, depth):
    global ans

    # N개의 방문지를 모두 돌았을 때
    if depth == N:
        distance += dist(now, end)
        ans = min(distance, ans)
        return

    # 백트래킹 : 중간 거리가 현재 정답보다 크다면 리턴(유망하지 않은 경로 더 이상 탐색하지 않음)
    if distance > ans:
        return

    # 탐색할 곳이 남았고 아직 유망한 경로 탐색
    for after in range(N):
        if not visited[after]:
            visited[after] = 1
            # now = 좌표
            dfs(house[after], distance + dist(now, house[after]), depth + 1)
            visited[after] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    coordinates = deque(list(map(int, input().split())))

    start = [coordinates.popleft(), coordinates.popleft()]
    end = [coordinates.popleft(), coordinates.popleft()]
    house = []  # N개의 집들이 담긴 이차원 리스트
    for _ in range(N):
        house.append([coordinates.popleft(), coordinates.popleft()])

        ans = 987654321
        visited = [0] * N

        dfs(start, 0, 0)

        print(f'{tc} {ans}')
