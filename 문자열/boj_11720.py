import sys

input = sys.stdin.readline

N = int(input())
total = sum(int(digit) for digit in input().rstrip())
print(total)
