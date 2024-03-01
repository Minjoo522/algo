H, M = map(int, input().split())

hour = 0
minute = 0

minutes_gap = M - 45
if minutes_gap < 0:
    minute = 60 + minutes_gap
    if H == 0:
        hour = 23
    else:
        hour = H - 1
else:
    hour = H
    minute = M - 45

print(f"{hour} {minute}")
