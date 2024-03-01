import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
sanggeun = list(map(int, input().split()))

M = int(input())
cards = list(map(int, input().split()))

dic = defaultdict(int)

for s in sanggeun:
    dic[s] += 1

print(' '.join(list(str(dic[i]) for i in cards)))
