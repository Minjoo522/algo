V, E = map(int, input().split())

adj_list = [[] for _ in range(V + 1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_list[start].append(end)
    adj_list[end].append(start)  # 양방향

stack = [1]
visited = []

while stack:
    current = stack.pop()
    if current not in visited:
        visited.append(current)

    for destination in adj_list[current]:  # 인접 리스트와 다른 부분
        if destination not in visited:
            stack.append(destination)

print('이동 경로: ', *visited)
