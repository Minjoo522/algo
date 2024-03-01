"""
쿼터 : 0.25
다임 : 0.10
니켈 : 0.05
페니 : 0.01

동전의 개수를 최소
"""
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    money = [25, 10, 5, 1]
    result = [0 for _ in range(4)]
    change = int(input())

    for i in range(4):
        result[i], change = divmod(change, money[i])

    print(*result)

# 방법 2
# for _ in range(int(input())):
#     money = [25, 10, 5, 1]
#     change = int(input())
#
#     result = [change // m for m in money]
#     print(*result)
