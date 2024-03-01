import sys

input = sys.stdin.readline

N = int(input())

total = 2 * N - 1
for j in range(1, total, 2):
    blank = (total - j) // 2
    print(f'{" " * blank}{"*" * j}')
for k in range(total, 0, -2):
    blank = (total - k) // 2
    print(f'{" " * blank}{"*" * k}')
