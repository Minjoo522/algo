# 누적 점수 = 0, 총 점수 = 0
# for문 돌며
# O이면 누적 점수 +1하고 총 점수 +누적 점수
# X이면 누적 점수 = 0
T = int(input())

for _ in range(T):
    total = 0
    current = 0
    for result in input():
        if result == 'O':
            current += 1
            total += current
        elif result == 'X':
            current = 0
    print(total)
