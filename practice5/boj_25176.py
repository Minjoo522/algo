"""
길이가 2N
1 ~ N까지의 정수들이 정확히 두 번 등장

점수 : 1이상 N이하인 모든 정수 i에 대해 다음 값의 합
(두 개의 i 사이에 있는 수의 합) × i
- 사이는 양끝의 i를 포함
"""
# 순열
import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(i)

count = 0
for i in permutations(arr, N):
    count += 1

print(count)
