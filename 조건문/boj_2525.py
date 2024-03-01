import sys

input = sys.stdin.readline

A, B = map(int, input().split())
C = int(input())
hour_add, minute_add = divmod(C, 60)  # (a // b, a % b)

new_hour = A + hour_add
new_minute = B + minute_add

if new_minute >= 60:
    new_hour += 1
    new_minute -= 60
if new_hour > 23:
    new_hour -= 24

print(new_hour, new_minute)
