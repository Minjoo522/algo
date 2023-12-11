"""
스도쿠❤️
<자료구조 모양>
1. 2차원 리스트 => 9 * 9

<로직>
1. 2차원 리스트 순회
2. 가로, 세로, 3 * 3칸 모두 1 ~ 9가 하나씩 존재하는지/중복 없이(set) 확인
    2.1 가로줄 숫자 모아 둔 set => 기존 리스트
    2.2 세로줄 숫자 모아 둔 set => 기존 리스트 zip 
    2.3 3*3 숫자 모아 둔 set
3. 이상 없으면 = 1, 있으면 = 0
"""


def check(sudoku):
    for line in sudoku:
        if len(set(line)) != 9:
            return False
    return True


for tc in range(1, int(input()) + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    sudoku2 = list(zip(*sudoku))
    sudoku3 = []

    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            tmp = []
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    tmp.append(sudoku[i][j])
            sudoku3.append(tmp)

    result = int(check(sudoku) and check(sudoku2) and check(sudoku3))
    print(f'#{tc} {result}')
