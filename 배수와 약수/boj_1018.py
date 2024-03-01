import sys

input = sys.stdin.readline


def check(test_case):
    cnt_1 = 0
    cnt_2 = 0
    origin_1 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
    origin_2 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']

    for r in range(8):
        for c in range(8):
            if test_case[r][c] != origin_1[r][c]:
                cnt_1 += 1
            if test_case[r][c] != origin_2[r][c]:
                cnt_2 += 1

    return min(cnt_1, cnt_2)


N, M = map(int, input().split())

matrix = [input().rstrip() for _ in range(N)]

ans = 987654321

for i in range(N - 7):
    for j in range(M - 7):
        board = []
        for r in range(8):
            board.append(matrix[i + r][j:j + 8])
        ans = min(ans, check(board))

print(ans)
