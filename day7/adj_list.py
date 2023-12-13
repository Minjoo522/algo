# 인접 리스트

V, E = map(int, input().split())

adj_list = [[] for _ in range(V + 1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_list[start].append(end)
    adj_list[end].append(start)  # 양방향

# [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
# 조회시 in 연산자 사용 ➡️ O(N)
# ✅ 조회가 많은 경우
# 리스트 안의 원소를 set으로
