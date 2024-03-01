"""
종말의 수 : 6이 적어도 3개 이상 들어가는 수
"""
import sys

input = sys.stdin.readline

N = int(input())
cnt = 0

for i in range(1, 2666800):
    if '666' in str(i):
        cnt += 1
    if cnt == N:
        print(i)
        break
