matrix = [[3, 7, 9], [4, 2, 6], [8, 1, 5]]
new_matrix = []

for m in matrix:
    new_matrix.append(m[:])

print(new_matrix)  # [[3, 7, 9], [4, 2, 6], [8, 1, 5]]

new_matrix2 = [m[:] for m in matrix]
