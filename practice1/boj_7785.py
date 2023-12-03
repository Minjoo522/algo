# 현재 회사에 있는 모든 사람 수
# n = 출입 기록의 수

# staffs = {}
# for문 돌며 출입 기록(name, status) 받기
# staffs[name] = status
# staffs의 values가 enter인 key들 리스트에 저장 => sorted, reverse = true

n = int(input())
staffs = {}

for i in range(n):
    name, status = input().split()
    staffs[name] = status

entered_staffs = sorted([name for name, status in staffs.items() if status == 'enter'], reverse=True)

for staff in entered_staffs:
    print(staff)