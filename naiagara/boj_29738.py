"""
Qualification Round, Round 1, Round 2, Round 3, World Finals
30점 이상을 획득하면 다음 라운드로 진출하는 Qualification Round와
더 이상 다음 라운드가 없는 World Finals
제외한 라운드는 다음 라운드에 진출하기 위해선 정해진 순위 안에 들어야 한다.

Round 1은 상위 4500등
Round 2는 상위 1000등
Round 3은 상위 25등 안에 들어야 다음 라운드에 진출

입력 : Google Code Jam 참가자가 가장 마지막으로 참가한 라운드의 등수 N

주어지는 참가자는 Qualification Round는 모두 통과했다고 가정
출력해야 할 라운드는 Round 1, Round 2, Round 3, World Finals 중 하나
"""
import sys

input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    rank = int(input())
    ans = ""

    if rank > 4500:
        ans = "Round 1"
    elif rank > 1000:
        ans = "Round 2"
    elif rank > 25:
        ans = "Round 3"
    else:
        ans = "World Finals"

    print(f"Case #{tc}: {ans}")
