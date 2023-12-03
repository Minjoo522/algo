# N개
# 1. for문을 N번 들며 들어가는 차량과 번호를 순서대로 딕셔너리에 저장한다
# 2. for문을 N번 돌며 나온 순서대로 들어왔던 번호를 리스트에 저장한다
# 리스트의 앞에 있는 차 번호가 뒤에 있는 차보다 크면 추월한 것 & 추월한 차들은 먼저 나온다(리스트의 앞쪽에 위치)
# 리스트를 거꾸로 돌기(기준 번호 갱신)
# 거꾸로 순회하면서(N-1 ~ 0)
# 리스트의 번호가 기준 번호보다 크면 == 추월한 것
# 아니면 추월하지 않았으니까 기준 번호 갱신

N = int(input())
count = 0

in_order = {}
for i in range(N):
    in_order[input()] = i

out_order = []
for _ in range(N):
    out_order.append(in_order[input()])

standard = N
for i in range(N-1, -1, -1):
    if out_order[i] > standard:
        count += 1
    else:
        standard = out_order[i]


print(count)