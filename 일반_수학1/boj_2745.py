"""
B진법 수를 10진법으로 바꾸기
"""
import sys

input = sys.stdin.readline

N, B = input().split()

print(int(N, int(B)))
