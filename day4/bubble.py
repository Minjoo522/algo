arr = [2, 4, 1, 3]

for i in range(len(arr) - 1, 0, -1):  # 총 3회 시행하는데 3, 2, 1 순서
    for j in range(i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
