import sys

sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N = int(input())
    price_flow = list(map(int, input().split()))

    max_p = 0
    profit = 0

    for p in price_flow[::-1]:
        # 최대 가격을 갱신하는 경우
        if p > max_p:
            max_p = p
        # 최대 가격을 갱신하지 못하는 경우
        else:
            profit += max_p - p

    print(f'#{tc} {profit}')
