import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = [[int(num) for num in input().split()] for _ in range(N)]
B = [[int(num) for num in input().split()] for _ in range(N)]
result = [list(map(lambda x, y: x + y, A, B)) for A, B in zip(A, B)]

for row in result:
    print(*row)
