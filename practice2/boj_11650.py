import sys
input = sys.stdin.readline

coordinates = [tuple(map(int, input().split())) for _ in range(int(input()))]
coordinates.sort()

for coordinate in coordinates:
    print(*coordinate)

# 이차원인 경우 sort만 해주면 둘 다 오름차순 조건이면 x 먼저, x가 같으면 y 오름차순으로 정렬이 잘 된다
