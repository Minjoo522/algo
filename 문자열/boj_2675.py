import sys

input = sys.stdin.readline

for _ in range(int(input())):
    R, S = input().split()
    result = ""

    for char in S:
        result += char * int(R)

    print(result)
