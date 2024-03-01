import sys

input = sys.stdin.readline

total_amount = int(input())

actual = 0

for _ in range(int(input())):
    price, quantity = map(int, input().split())
    actual += price * quantity

if total_amount == actual:
    print("Yes")
else:
    print("No")
