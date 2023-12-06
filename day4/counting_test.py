nums = [4, 4, 2, 3, 5, 5, 1, 1, 5]

count = [0] * (max(nums) + 1)  # 각각 숫자가 몇 개씩 있는지 개수 세기
sorted_nums = [0] * len(nums)  # 정렬된 리스트 틀

for num in nums:
    count[num] += 1
    
for i in range(1, len(count)):  # 누적합
    count[i] = count[i] + count[i-1]
    
for j in range(len(nums)-1, -1, -1):
    sorted_nums[count[nums[j]] - 1] = nums[j]
    count[nums[j]] -= 1
    
print(sorted_nums)