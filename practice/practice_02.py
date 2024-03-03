nums = [7, 1, 2, 4, 6, 8, 3]

max_num = -1
for num in nums:
    if num > max_num:
        max_num = num

print(max_num)

min_num = 987654321
for num in nums:
    if num < min_num:
        min_num = num

print(min_num)
