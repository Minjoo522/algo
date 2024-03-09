matrix = [[3, 7, 9],
          [4, 2, 6],
          [8, 1, 5]]


# for r in range(3):
#     for c in range(3):
#         if r > c:
#             matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
# # [[3, 4, 8], [7, 2, 1], [9, 6, 5]]
#
# print(matrix)

zipped_matrix = list(map(list, zip(*matrix)))
# [[3, 4, 8], [7, 2, 1], [9, 6, 5]]
# [(3, 4, 8), (7, 2, 1), (9, 6, 5)]
print(zipped_matrix)
