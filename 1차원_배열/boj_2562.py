import sys

input = sys.stdin.readline

max_value = 0
index = 0

for i in range(1, 10):
    num = int(input())
    if num > max_value:
        max_value = num
        index = i

print(max_value)
print(index)
