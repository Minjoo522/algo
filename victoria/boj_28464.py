"""
N개의 접시
i번째 접시, a(i)개의 감자튀김
책상 위에 남아있는 접시 하나를 고르고, 접시와 그 위에 놓인 모든 감자튀김을 가져간다.
책상 위의 접시가 모두 사라질 때까지 반복
맨 처음 접시를 가져가는 사람은 박 모 씨

박 모 씨는 가져가는 감자튀김의 양을 최대화
성우는 가져가는 감자튀김의 양을 최소화

최종적으로 가져가는 감자튀김의 양 => 성우 / 박모
"""
import sys

input = sys.stdin.readline

N = int(input())
plates = list(map(int, input().split()))

park = 0
sungwoo = 0

while sum(plates) != 0:
    park_pick_count = max(plates)
    park += park_pick_count
    plates.pop(plates.index(park_pick_count))
    if sum(plates) == 0:
        break
    sungwoo_pick_count = min(plates)
    sungwoo += sungwoo_pick_count
    plates.pop(plates.index(sungwoo_pick_count))

print(sungwoo, park)
