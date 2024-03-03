gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]

# 1등급 광물이 존재하는지 여부
if 1 in gems:
    print(True)
else:
    print(False)

# 플래그 사용
grade1 = False
for i in gems:
    if i == 1:
        grade1 = True
        break

print(grade1)

# 1, 2, 3 등급 광물은 각각 몇 개가 있는지
grades = {1: 0, 2: 0, 3: 0}

for i in gems:
    grades[i] += 1

print(grades)

# 등급에 따른 성공 척도
result = sum(gems)

if result <= 15:
    print("성공")
elif 15 < result <= 23:
    print("보통")
else:
    print("실패")
