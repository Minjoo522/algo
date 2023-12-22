arr = ['A', 'B', 'C']

for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and k != i:
                print([arr[i], arr[j], arr[k]])
