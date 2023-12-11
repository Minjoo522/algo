"""
<로직>
** 재귀
1. 현재 전체 종이가 같은 색으로 칠해져 있는지 확인
2. 잘라진 종이가 모두 하얀색이나 파란색인지 확인
    => 순회하면서 다른 색이 나오는지 확인
4. 아니면, 4등분(재귀)
5. 하얀색 색종이 개수, 파란색 색종이 개수 순서대로 출력
"""

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0


def make_colored_paper(r, c, n):
    global white, blue

    cnt = board[r][c]

    for i in range(r, r + n):
        for j in range(c, c + n):
            if cnt != board[i][j]:
                make_colored_paper(r, c, n // 2)
                make_colored_paper(r, c + n // 2, n // 2)
                make_colored_paper(r + n // 2, c, n // 2)
                make_colored_paper(r + n // 2, c + n // 2, n // 2)
                return

    if cnt == 0:
        white += 1
    else:
        blue += 1


make_colored_paper(0, 0, N)
print(white)
print(blue)
