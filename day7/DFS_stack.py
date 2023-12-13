V, E = map(int, input().split())  # Vertex, Edge 개수

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

for _ in range(E):  # 간선 갯수만큼 돌면서 연결 정보를 받음
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1  # 양방향 그래프니까

stack = [1]
visited = []

while stack:  # 스택이 빌 때까지
    current = stack.pop()
    if current not in visited:
        visited.append(current)

    for destination in range(V + 1):
        if adj_matrix[current][destination] and destination not in visited:
            # 갈 수 있고 + 방문하지 않은 곳
            stack.append(destination)

print('이동 경로: ', *visited)
# 이동 경로:  1 3 7 6 5 2 4
