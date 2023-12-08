matrix = [[3, 7, 9],
          [4, 2, 6],
          [8, 1, 5]]

for r in range(3):
    for c in range(3):  # 행 우선 순회 코드
        if r > c:  # r < c도 됨(but 한 번만 해야함) / r == c는 [0][0], [1][1], [2][2]
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
