arr = ['A', 'B', 'C', 'D', 'E']
sel = [0, 0, 0]


def combinstion(idx, sidx):
    # sidx, idx 조건 확인하는 건 자리 서로 바뀌면 안됨!
    if sidx == 3:
        print(sel)
        return

    if idx == 5:
        return

    sel[sidx] = arr[idx]
    combinstion(idx + 1, sidx + 1)
    combinstion(idx + 1, sidx)


combinstion(0, 0)
