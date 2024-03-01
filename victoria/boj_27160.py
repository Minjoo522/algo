import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
dic = defaultdict(int)

for _ in range(N):
    fruit, count = input().rstrip().split()
    dic[fruit] += int(count)

found = False
for index, value in dic.items():
    if value == 5:
        print("YES")
        found = True
        break

if found == False:
    print("NO")
