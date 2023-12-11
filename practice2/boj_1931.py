"""
1. 종료 시간 순으로 정리
2. 종료 시간이 같은 경우 시작시간이 빠른 순서대로 정리
3. 기준 시간 첫 회의 종료 시간으로 갱신
4. 다음 회의 시작 시간이 기준 시간 이후면 cnt += 1
"""

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

meetings.sort(key=lambda x: (x[1], x[0]))

standard = 0
result = 0

for start, end in meetings:
    if start >= standard:
        standard = end
        result += 1

print(result)
