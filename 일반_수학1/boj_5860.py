"""
V 미터 나무 막대

낮 : A 미터 올라감
밤 : B 미터 내려감

정상에 올라간 후에는 미끄러지지 않는다
막대를 모두 올라가려면 며칠이 걸리는가?

# 하루 동안 올라갈 수 있는 거리: A - B
# 목표 지점 V에 도달하기 위해 필요한 총 거리: V - A
# 낮과 밤의 이동 거리 차이로 인해 목표 지점에 도달하기까지의 일 수 계산
"""
import sys
import math

input = sys.stdin.readline

A, B, V = map(int, input().split())
days = math.ceil((V - A) / (A - B)) + 1

print(days)
