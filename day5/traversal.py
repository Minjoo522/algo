matrix = [[3, 7, 9],
          [4, 2, 6],
          [8, 1, 5]]

# 행 우선 순회
for r in range(3):
    for c in range(3):
        print(matrix[r][c])  # 3 7 9 4 2 6 8 1 5
        
# 열 우선 순회
for r in range(3):
    for c in range(3):
        print(matrix[c][r])  # 3 4 8 7 2 1 9 6 5
