"""
중앙 1부터 시작 이웃하는 방에 돌아가면서 1씩 증가
1 ~ N번 방까지 최소개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지

cnt = 1
1 -> 7 -> 19 -> 37 -> 61
=> 6 -> 12 -> 18 -> 24(6 * n만큼 증가)

f(n) = f(n - 1) + 6 * n
"""
import sys

input = sys.stdin.readline

n = int(input())

total = 1
cnt = 1
while n > total:
    total += 6 * cnt
    cnt += 1
print(cnt)
