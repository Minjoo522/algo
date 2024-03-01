"""
숫자가 들어왔다면 그 숫자에 해당하는 포켓몬의 이름을, 문자가 들어왔으면 그 포켓몬의 이름에 해당하는 번호를 출력
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pocketmons = {}

for i in range(1, N + 1):
    pocketmon = input().rstrip()
    pocketmons[pocketmon] = i
    pocketmons[str(i)] = pocketmon

for _ in range(M):
    print(pocketmons[input().rstrip()])
