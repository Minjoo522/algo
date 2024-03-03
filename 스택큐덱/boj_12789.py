"""
문제를 잘 읽자!
쭉 넣고 끝에서 빠져나올 수 있음
target은 1부터 순차적으로 증가
"""

import sys

input = sys.stdin.readline

N = int(input())
current = list(map(int, input().split()))
tmp = []
target = 1

for i in current:
    tmp.append(i)
    while tmp and tmp[-1] == target:
        tmp.pop()
        target += 1
    if len(tmp) > 1 and tmp[-1] > tmp[-2]:  # 스택의 제일 위가 그 아래보다 크면 작은 애가 빠져나올 수 없음
        print('Sad')
        sys.exit()
if tmp:
    print('Sad')
else:
    print('Nice')
