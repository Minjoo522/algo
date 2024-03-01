import sys

input = sys.stdin.readline

N = int(input())


def check(sugar):
    cnt = 987654321

    for i in range(sugar // 5 + 1):
        current = sugar - 5 * i
        for j in range(current // 3 + 1):
            if current - j * 3 == 0:
                cnt = min(cnt, i + j)

    if cnt == 987654321:
        return -1
    return cnt


print(check(N))
