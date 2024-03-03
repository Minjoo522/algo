import sys
from collections import deque

input = sys.stdin.readline

def findVPS(PS):
    if PS[0] == ')':
        return 'NO'

    stack = deque()
    for ps in PS:
        if ps == '(':
            stack.append(ps)
        if ps == ')':
            if len(stack) == 0:
                return 'NO'
            else:
                stack.pop()

    if len(stack) != 0:
        return 'NO'
    return 'YES'


for _ in range(int(input())):
    PS = deque(input().rstrip())
    print(findVPS(PS))
