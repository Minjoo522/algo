import sys

input = sys.stdin.readline

N = int(input())

gomgom = set()
cnt = 0

for _ in range(N):
    command = input().rstrip()
    if command == "ENTER":
        gomgom.clear()
    elif command not in gomgom:
        gomgom.add(command)
        cnt += 1

print(cnt)
