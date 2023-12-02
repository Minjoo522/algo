T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    chargers = list(map(int, input().split()))
    current = K
    count = 0
    for i in range(1, N + 1):
        current -= 1
        if i in chargers:
            charger_idx = chargers.index(i)
            remain_chargers = chargers[charger_idx + 1:]
            if len(remain_chargers) > 0:
                if current - (remain_chargers[0] - i) >= 0:
                    continue
                else:
                    if K - (remain_chargers[0] - i) < 0:
                        count = 0
                        break
                    else:
                        current = K
                        count += 1
            else:
                if current - (N - i) >= 0:
                    continue
                else:
                    if K - (N - i) < 0:
                        count = 0
                        break
                    else:
                        current = K
                        count += 1
    print(f'#{tc} {count}')
