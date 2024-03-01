import sys

input = sys.stdin.readline

N = int(input())
s = input().rstrip()

jaeum = ['r', 's', 'e', 'f', 'a', 'q', 't', 'd', 'w', 'c', 'z', 'x', 'v', 'g']
end_s = s[-1]

if end_s in jaeum:
    print(1)
else:
    print(0)
