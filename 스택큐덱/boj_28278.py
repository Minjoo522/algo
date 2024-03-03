"""
1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다. // 나중에 넣은 것
3: 스택에 들어있는 정수의 개수를 출력한다.
4: 스택이 비어있으면 1, 아니면 0을 출력한다.
5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
"""
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
stack = deque()

for _ in range(N):
    line = input().rstrip()
    command = int(line[0])
    if command == 1:
        stack.append(int(line[2:]))
    elif command == 2:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command == 3:
        print(len(stack))
    elif command == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
