import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
ans = []

while q:
    idx, paper = q.popleft();
    ans.append(idx + 1)

    if paper > 0:
        q.rotate(-(paper - 1))  # 현재 풍선을 pop했기 때문에 왼쪽으로 1칸씩 회전된 상태
    elif paper < 0:
        q.rotate(-paper)

print(*ans)

# 터진 풍성의 번호(인덱스 + 1)을 출력하는 문제
# 초기 인덱스 정보 끝까지 유지 -> enumerate
# 튜플로 (인덱스, 값)을 묶기
# deque의 rotate -> 회전(default = 오른쪽, - = 왼쪽)
