"""
인접 리스트 + DFS(stack)
컴퓨터의 수 = 1부터 시작(0 ~ N + 1)

1. 인접 리스트 생성
2. stack 1부터 시작
3. visited에 1 넣어두기
4. stack이 빌 때까지 반복
    4.1 현재 스택의 제일 위에 있는 걸 뺀다(인덱스)
    4.2 그 컴퓨터의 리스트를 순회한다
    4.3 방문하지 않았다면 stack에 추가해주고 visited에 추가한다
"""
import sys

input = sys.stdin.readline

N = int(input())
E = int(input())

computers = [[] for _ in range(N + 1)]
for _ in range(E):
    start, end = map(int, input().split())
    computers[start].append(end)
    computers[end].append(start)

stack = [1]
visited = set([1])

while stack:
    current = stack.pop()

    for computer in computers[current]:
        if computer not in visited:
            stack.append(computer)
            visited.add(computer)

print(len(visited) - 1)
