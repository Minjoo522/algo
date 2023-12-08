N = 3
matrix = [[3, 7, 9],
          [4, 2, 6],
          [8, 1, 5]]

# 행 우선 순회
for i in range(N ** 2):
    print(matrix[i // N][i % N])
