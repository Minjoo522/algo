# N, M = 포켓몬의 개수, 맞춰야하는 문제의 개수
# poketmons = {}
# N만큼 돌며 포켓몬 이름 받아서 딕셔너리에 포켓몬이름: 번호, 번호: 포켓몬이름 저장 -> 시간 초과 방지 위하여 둘 다 저장
# M만큼 돌며 문제 하나씩 풀기
# key로 찾아서 값 출력
import sys

input = sys.stdin.readline
N, M = list(map(int, input().split()))
poketmons = {}

for i in range(N):
    poketmon = input().strip()
    poketmons[poketmon] = str(i + 1)
    poketmons[str(i + 1)] = poketmon

for _ in range(M):
    print(poketmons[input().strip()])
