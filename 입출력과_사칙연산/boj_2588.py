import sys
input = sys.stdin.readline

X = int(input())
Y = input().rstrip()

for i in range(len(Y) - 1, -1, -1):
    print(X * int(Y[i]))

print(X * int(Y))
