# 생성자 + 생성자의 각 자리 수의 합 = N
# 생성자는 N보다 작음
# 생성자는 N에서 각 자리 수 합의 최대값을 뺀 것보다 크거나 같음
# 자리 수가 3일 때 각 자리수 합의 최대값 = 9 + 9 + 9
# 예) 216 - 27 = 189
# 189 ~ 216까지 for문 돌면서 확인
N = int(input())
digit = len(str(N))
start = max(1, N - (9 * digit), 1)
result = 0

for i in range(start, N + 1):
    digit_sum = sum(map(int, str(i)))
    if i + digit_sum == N:
        result = i
        break

print(result)
