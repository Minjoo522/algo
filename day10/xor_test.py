nums = [4, 2, 3, 1, 3, 1, 4]
nums = [77, 26, 34, 5, 5, 26, 34, 17, 24, 17, 24]
nums_set = set(nums)
for num in nums_set:
    if nums.count(num) == 1:
        print(num)

# 1. 리스트 집계
# max 값 찾기 => max 값을 인덱스로 갖는 리스트 만들어서 집계
# 리스트가 엄청 커질 수 있음

# 2. dict 집계
# 공간 복잡도 큼

# 3. set 중복 제거 + count
# set을 만드는 데 오래 걸림
# 돌면서 count => 시간 복잡도 큼

# 4. sort
# O(NlogN)

# 5. xor
# O(N)
answer = 0
for num in nums:
    answer ^= num
print(answer)

alphabets = ['a', 'b', 'c']