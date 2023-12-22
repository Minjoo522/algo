arr = ['A', 'B', 'C']
sel = [0, 0, 0]
check = [0, 0, 0]


def perm(depth):
    if depth == 3:
        print(sel)
        return

    for i in range(3):
        if not check[i]:  # 화살표가 멈출 수 있으면(아무도 쓰지 않고 있는 자리이면)
            check[i] = 1
            sel[depth] = arr[i]
            perm(depth + 1)
            check[i] = 0  # 🚨 돌아 나오면서 다시 다음을 위해 초기화!


perm(0)
