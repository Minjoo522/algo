import sys

input = sys.stdin.readline

while True:
    line = input().rstrip()
    if not line:
        break
    print(line)
