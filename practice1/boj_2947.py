nums = list(map(int, input().split()))

while nums != [1, 2, 3, 4, 5]:
    for i in range(1, 5):
        if nums[i - 1] > nums[i]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
            print(' '.join(map(str, nums)))