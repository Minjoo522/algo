"""
그리디 : 현재시점에서 최적화 / 부분 최적화가 전체 최적화를 담보
- 정렬 / heap

끝나는 시간과 시작 시간이 같으면 같은 강의실 사용 가능

⭐️ 그리디 문제는 첫 번째 강의부터 생각하기!

- 시작하는 시간이 중요
- 가장 빨리 시작하는 강의부터 : 시작 순서로 정렬
- 일단 집어 넣어봄
- 끝나는 시간의 최소값(standard)과 시작하는 시간의 최소값을 비교

⭐️ standard 갱신 로직 : heap
"""
from collections import deque
from heapq import heappush, heappop

N = int(input())

lectures = deque(sorted(list(tuple(map(int, input().split())) for _ in range(N))))
heap = []
heappop(heap, lectures.popleft()[1])

while lectures:
    s, e = lectures.popleft()

    standard = heappop(heap)  # 강의 종료 시간이 heap에 들어감

    if s >= standard:
        heappush(heap, e)

    else:
        heappush(heap, standard)  # heappop한 거 다시 넣음(다음 강의 못 넣었으니까)
        heappush(heap, e)  # 강의실 하나 더 사용

print(len(heap))  # heap에는 각 강의실의 마지막 강의가 담김
