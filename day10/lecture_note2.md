# 순열, 조합
- 순열(permutation) : 순서 ⭕️
- 조합(combination) : 순서 ❌
- 중복 순열
- 중복 조합

# 조합
## nC2
- 이중 for문
~~~python
# 그냥 조합 2개뽑기
arr = ['A', 'B', 'C']
for i in range(3):
    for j in range(i+1, 3):
        print(arr[i], arr[j])

# 중복조합 2개뽑기
arr = ['A', 'B', 'C']
for i in range(3):
    for j in range(i, 3):
        print(arr[i], arr[j])
~~~

## 재귀
~~~python
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
~~~

# 모듈
~~~python
from itertools import combinations, permutations

arr = ['A', 'B', 'C']
for x, y in combinations(arr, 2):  # 3C2
    print(x, y)

for z, w in permutations(arr, 2):  # 3P2
    print(z, w)
~~~