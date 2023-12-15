dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                initial_r, initial_c = i, j
            elif arr[i][j] == 3:
                final_r, final_c = i, j

    stack = [[initial_r, initial_c]]
    visited = set()
    visited.add((initial_r, initial_c))
    answer = 0

    while stack:
        r, c = stack.pop()
        if r == final_r and c == final_c:
            answer = 1
            break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < 16 and 0 <= nc < 16 and arr[nr][nc] != 1 and (nr, nc) not in visited:
                # visited add와 stack에 넣는 것을 동시에(중복되지 않도록)
                visited.add((nr, nc))
                stack.append([nr, nc])

    print(f'#{tc} {answer}')