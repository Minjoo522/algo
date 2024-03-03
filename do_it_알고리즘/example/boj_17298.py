import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
ans = [0] * n
my_stack = []

for i in range(n):
    while my_stack and A[my_stack[-1]] < A[i]:
        ans[my_stack.pop()] = A[i]
    my_stack.append(i)

while my_stack:
    ans[my_stack.pop()] = -1

print(*ans)
