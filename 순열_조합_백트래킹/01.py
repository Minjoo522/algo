arr = ['A', 'B', 'C']  # 재료 리스트
check = [0, 0, 0]  # 위치 체크용 리스트


def powerset(idx):
    if idx == 3:
        print('체크 배열은 다음과 같음: ', *check)
        result = []
        for j in range(3):
            if check[j] == 1:
                result.append(arr[j])
        print(result)
        return

    check[idx] = 0
    powerset(idx + 1)

    check[idx] = 1
    powerset(idx + 1)


powerset(0)

"""
0 : check[0] = 0 / check[0] = 1
1 : check[1] = 0 / check[1] = 1 / check[1] = 0
2 : check[2] = 0 / check[2] = 1 / check[2] = 0 / check[2] = 1 / check[2] = 0 / check[2] = 1
3 : 0, 0, 0 - [] 리턴 / 0, 0, 1 - ['C'] 리턴 / 0, 1, 0 - ['B'] 리턴 / 0, 1, 1 - ['B', 'C'] 리턴 / 1, 0, 0 - ['A'] / 1, 0, 1 - ['A', 'C']
"""