nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binary_search(low, high, target):
    if low > high:  # 포인터 크로스
        return '찾지 못함'

    mid = (low + high) // 2
    if target == nums[mid]:
        return mid
    elif target < nums[mid]:
        return binary_search(low, mid - 1, target)
    elif target > nums[mid]:
        return binary_search(mid + 1, high, target)


print(binary_search(0, len(nums) - 1, 7))
