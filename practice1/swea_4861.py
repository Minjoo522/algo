# 회문
# N x N 크기의 글자판
# 길이가 M인 회문 찾아 출력
# 세로로 찾을 수도 있음

# 회문은 1개 존재 = 회문 찾으면 바로 종료
# N개 문자 for문 돌아가며 받아서 list에 저장
# 가로 회문 찾기
# 방법 1 : 문자를 한 줄 한 줄 받을 때마다 회문 검사한다
# 방법 2 : 문자를 리스트에 전부 저장한 뒤 리스트를 돌면서 회문 검사한다
# for문 N-M+1만큼 돌며 슬라이싱 후 회문 검사
# 세로 회문 찾기
# 세로 조합 - zip(*문자들)
# for문 N-M+1만큼 돌며 슬라이싱 후 회문 검사
T = int(input())


def find_palindrome(lines):
    for line in lines:
        for i in range(N - M + 1):
            target = line[i:i + M]
            if target == target[::-1]:
                return target
    return ''


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lines = [input() for _ in range(N)]
    if find_palindrome(lines):
        print(f'#{tc} {find_palindrome(lines)}')
        continue

    rotated_lines = [''.join(line) for line in zip(*lines)]
    if find_palindrome(rotated_lines):
        print(f'#{tc} {find_palindrome(rotated_lines)}')
