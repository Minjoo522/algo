b = [[0] * 3] * 3  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
b[0][0] = 9  # [[9, 0, 0], [9, 0, 0], [9, 0, 0]]

c = [[1, 2], [3, 4]]
d = c[:]  # shallow copy : [[1, 2], [3, 4]]
c[1][1] = 5
print(d)  # [[1, 2], [3, 5]]