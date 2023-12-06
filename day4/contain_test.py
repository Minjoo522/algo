t = 'hello world'
p = 'wor'


def find_word(p, t):
    N = len(t)
    M = len(p)

    for i in range(N - M + 1):
        cnt = 0
        for j in range(M):
            if t[i + j] == p[j]:  # 포인터를 t에 하나 p에 하나 두는 것
                cnt += 1
            else:
                break

        if cnt == M:
            return i

    return '못찾았음'


print(find_word(p, t))
