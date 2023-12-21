import sys
input = sys.stdin.readline

nums = sorted(int(input()) for _ in range(int(input())))

for num in nums:
    print(num)
