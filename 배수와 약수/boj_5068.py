"""
첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither
"""
import sys

input = sys.stdin.readline

while True:
    A, B = map(int, input().split())

    if A == 0 and B == 0:
        break

    if B % A == 0:
        print("factor")
    elif A % B == 0:
        print("multiple")
    else:
        print("neither")
