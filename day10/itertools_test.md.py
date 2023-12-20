from itertools import combinations, permutations

arr = ['A', 'B', 'C']
for x, y in combinations(arr, 2):  # 3C2
    print(x, y)

for z, w in permutations(arr, 2):  # 3P2
    print(z, w)
