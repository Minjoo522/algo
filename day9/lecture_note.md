## deque
~~~python
# 1부터 N까지 deque가 생성됨
queue = deque(range(1, N+1))
queue.append(queue.popleft())
~~~

## 그래프 구조화
- 인접 행렬 vs 인접 리스트
- 인접 행렬 : 공간 복잡도 큼
- 인접 리스트가 인접 행렬보다 빠름

## 패딩
- 필드를 다른 걸로 감싸는 것
- 복잡한 문제일수록 조금 더 빠르긴 함
~~~python
[['#' for _ in range(C+2) for _ in range(R+2)]
~~~

## 암시적 그래프 표현
- 이차원 리스트를 직접 만들지 않고 집합 안에 tuple 형태로 좌표를 넣음
- 집합 자체가 하나의 그래프가 됨
- 그래프의 크기가 크고 좌표가 많지 않거나 마이너스 좌표를 사용해야 할 때
~~~python
import sys

input = sys.stdin.readline

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def BFS(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if (nx, ny) in cabbages:
                queue.append((nx, ny))
                cabbages.discard((nx, ny))


for _ in range(int(input())):
    M, N, K = map(int, input().split())
    cabbages = set(tuple(map(int, input().split())) for _ in range(K))
    ans = 0

    while cabbages:
        i, j = cabbages.pop()
        BFS(i, j)
        ans += 1

    print(ans)
~~~