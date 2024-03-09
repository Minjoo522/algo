matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = 3

# for i in range(n):
#     for j in range(n):
#         rotated_matrix[i][j] = matrix[j][n-i-1]  # 1을 빼는 이유 : 마지막 행의 번호는 n이 아니라 n-1
# # [[3, 6, 9], [2, 5, 8], [1, 4, 7]]

rotated_matrix = list(zip(*matrix))[::-1]
# [(3, 6, 9), (2, 5, 8), (1, 4, 7)]

print(rotated_matrix)

ways = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
]
