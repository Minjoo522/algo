"""
<로직> - 이진 탐색
low, high, target
1. A, B 각각 검색 시작
    1.1 mid == target: 검색 종료
    1.2 mid > target: right = mid
    1.3 mid < target: left = mid
2. 매번 A, B 각각의 검색 횟수 갱신
3. A, B 중 검색 횟수 비교
"""


def search(left, right, target):
    cnt = 0

    while True:
        mid = int((left + right) / 2)

        if mid == target:
            break
        elif mid > target:
            right = mid
        elif mid < target:
            left = mid

        cnt += 1

    return cnt


for tc in range(1, int(input()) + 1):
    P, Pa, Pb = map(int, input().split())

    A = search(1, P, Pa)
    B = search(1, P, Pb)

    result = 'A' if A < B else ('B' if A > B else 0)

    print(f'#{tc} {result}')
