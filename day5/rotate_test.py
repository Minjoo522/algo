matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# n = 3
# rotated_matrix = [[0] * n for _ in range(n)]
# 
# for i in range(n):
#     for j in range(n):
#         rotated_matrix[i][j] = matrix[n-j-1][i]  # 원본 리스트 : 열 우선 순회

rotated_matrix = list(zip(*matrix[::-1]))
print(rotated_matrix)  # [(7, 4, 1), (8, 5, 2), (9, 6, 3)]