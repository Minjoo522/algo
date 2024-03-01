import sys
from collections import defaultdict

input = sys.stdin.readline

word = input().rstrip().upper()
dic = defaultdict(int)

for w in word:
    dic[w] += 1

max_val = max(dic.values())
max_str = [key for key, value in dic.items() if value == max_val]

if len(max_str) > 1:
    print("?")
else:
    print(max_str[0])
