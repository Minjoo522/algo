from collections import deque

n, k = map(int, input().split())
people = list(i for i in range(n + 1))
result = deque()

while len(people) > 1:
    if len(people) < k + 1:
        result.append(people.pop(1))
    else:
        result.append(people.pop(k))

print(result)

"""
그 번호부터 k번째
현재 인덱스 번호 알아야 함
3 * index % n

1, 2, 3, 4, 5, 6, 7

3
1, 2, 4, 5, 6, 7

6
1, 2, 4, 5, 7

2
1, 4, 5, 7

7
1, 4, 5

6
1, 4
"""