import sys

input = sys.stdin.readline

N, B = map(int, input().split())

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

current = N
result = ""
count = 1

while current > 0:
    current, remainder = divmod(current, B)  # a를 b로 나눈 몫과 나머지를 반환
    result = digits[remainder] + result
    print(f"{count}번 째 :")
    print(f"몫 : {current}")
    print(f"나머지: {remainder}")
    print(f"digit: {digits[remainder]}")
    print(f"현재 결과: {result}")
    count += 1

print(result)
