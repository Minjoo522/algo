# 오르막길, 내리막길, 평지
# 큰 오르막길의 길이
# 측정한 높이 : 길이가 N인 수열
# 오르막길 : 적어도 2개의 수로 이루어진 높이가 증가하는 부분 수열
# 오르막길의 크기 : 부분 수열의 첫 번째 숫자와 마지막 숫자의 차이

# now, max = 0
# roads들을 1 ~ N까지 순회
# 뒤 > 앞이면 == 오르막길이면
# 올라간만큼(뒤 - 앞) now에 추가
# max(현재 max, now) → max 값 갱신
# 뒤 > 앞이 아니면
# now = 0 초기화
N = int(input())
roads = list(map(int, input().split()))
now, max_height = 0, 0

for i in range(1, N):
    if roads[i] > roads[i - 1]:
        now += roads[i] - roads[i - 1]
        max_height = max(max_height, now)
    else:
        now = 0

print(max_height)
