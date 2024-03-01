import sys

input = sys.stdin.readline

A, B = map(int, input().split())
print(f'{A + B}\n{A - B}\n{A * B}\n{A // B}\n{A % B}')
