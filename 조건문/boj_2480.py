"""
1. 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
2. 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
3. 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
"""
import sys
from collections import defaultdict

input = sys.stdin.readline

nums = list(map(int, input().split()))

counts = defaultdict(int)

for num in nums:
    counts[num] += 1

max_value = 0
max_key = ""

for key, value in counts.items():
    if value > max_value:
        max_value = value
        max_key = key

if max_value == 3:
    print(f"{10000 + int(max_key) * 1000}")
elif max_value == 2:
    print(f"{1000 + int(max_key) * 100}")
else:
    print(f"{max(nums) * 100}")
