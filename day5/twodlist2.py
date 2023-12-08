a = []

for i in range(3):
    b = [0] * 3
    a.append(b)

print(a)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
a[0][0] = 9
print(a)  # [[9, 0, 0], [0, 0, 0], [0, 0, 0]]

# ✨ list comprehension
c = [[0] * 3 for _ in range(3)]  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
