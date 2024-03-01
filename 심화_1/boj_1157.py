import sys
from collections import defaultdict

input = sys.stdin.readline

word = input().rstrip().upper()

count = defaultdict(int)
for char in word:
    count[char] += 1

max_count = max(count.values())
max_alphabet = [key for key, value in count.items() if value == max_count]

if len(max_alphabet) > 1:
    print('?')
else:
    print(max_alphabet[0])
