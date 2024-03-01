import sys

input = sys.stdin.readline

for _ in range(int(input())):
    word = input().rstrip()
    print(word[0] + word[-1])
