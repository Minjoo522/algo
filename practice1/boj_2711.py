# 오타를 지운 문자열을 출력
# 첫 숫자 : 오차를 낸 위치
# 두 번째 문자열 : 창영이가 친 문자
# 슬라이싱으로 해당 문자 제외하고 더하기

T = int(input())
for _ in range(T):
    position, word = input().split()
    position = int(position)
    print(word[:position - 1] + word[position:])