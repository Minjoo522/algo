"""
글자 수만큼 아래를 반복한다
1. 닫는 괄호가 제일 먼저 나오면 for문을 종료하고 NO
2. 여는 괄호가 나오면 여는 괄호를 stack에 넣어준다
3. 닫는 괄호가 나오면 stack에 있는 여는 괄호를 하나 빼준다
    3.1 여는 괄호가 없다면 for문을 종료하고 NO
반복 후 stack에 남아 있는 여는 괄호가 있다면 NO
"""


def findVPS(PS):
    if PS[0] == ')':
        return 'NO'

    stack = []
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


T = int(input())

for _ in range(T):
    PS = list(input())
    print(findVPS(PS))
