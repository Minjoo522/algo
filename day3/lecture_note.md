# 컴퓨터처럼 생각하기
- 일일이 다 계산하고 개선해 나가기

# 1. 구간합
## 브루트포스 : 모든 경우의 수 다 해보기(완전 탐색)
## 슬라이딩 윈도우
## 누적합
~~~python
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input()))
    s = 0
    S = [0]

    for num in nums:
        s += num
        S.append(s)

    prefix_sum = []

    for i in range(M, N+1):
        prefix_sum.append(S[i] - S[i-M])
        
    max_sum = max(prefix_sum)
    min_sum = min(prefix_sum)
    
    print(f'#{tc} {max_sum - min_sum}')
~~~

# 2. 베스트셀러
## defaultdict
- 유사 dict
- value 값이 default로 정해져있
- 그냥 dict는 없는 key로 검색할 때 keyError 발생하지만 defaultdict는 발생하지 않음
~~~python
from collections import defaultdict

my_dict1 = defaultdict(int)
my_dict2 = defaultdict(str)
my_dict3 = defaultdict(list)
my_dict4 = defaultdict(set)

print(my_dict1)
print(my_dict2)
print(my_dict3)
print(my_dict4)
# defaultdict(<class 'int'>, {})
# defaultdict(<class 'str'>, {})
# defaultdict(<class 'list'>, {})
# defaultdict(<class 'set'>, {})

# 없는 key로 검색해도 기본값을 만들어서 생성해줌
print(my_dict1['my_key'])  # 0
print(my_dict2['my_key'])
print(my_dict3['my_key'])  # []
print(my_dict4['my_key'])  # set()
print(my_dict1)  # defaultdict(<class 'int'>, {'my_key': 0})
print(my_dict2)  # defaultdict(<class 'str'>, {'my_key': ''})
print(my_dict3)  # defaultdict(<class 'list'>, {'my_key': []})
print(my_dict4)  # defaultdict(<class 'set'>, {'my_key': set()})

# 활용
my_dict5 = defaultdict(int)
my_dict5['my_key'] += 1
print(my_dict5)  # defaultdict(<class 'int'>, {'my_key': 1})
print(my_dict5['my_key'])  # 1
~~~

## 딕셔너리 정렬
- sorted 사용 가능
~~~python
books_sales_info = defaultdict(int)
books_sales_info = dict(sorted(books_sales_info.items()))
# sorted : 튜플이 담긴 리스트 반환 => 다시 dict로 변환
~~~

## sorted, key = lambda
- sorted(itrable 객체, key=lambda 변수 : 정렬 기준)
- 기준이 두개 이상인 경우 튜플로 묶어서 정렬 => 우선순위는 앞 쪽이 먼저
~~~python
books_sales_info = sorted(books_sales_info.items(), key=lambda x : (-x[1], x[0])
# -x? : value가 -를 붙였을 때 큰 것부터 앞으로
~~~
- 내림차순 정렬 : lambda 사용 x => reverse=True
~~~python
my_dict = {'c': 5, 'a': 5, 'b': 3, 'e': 4, 'd': 3}
# print(sorted(my_dict))  # ['a', 'b', 'c', 'd', 'e']
print(sorted(my_dict.items()))  # [('a', 5), ('b', 3), ('c', 5), ('d', 3), ('e', 4)] ✅ key 값 순서로 정렬
print(sorted(my_dict.items(), key=lambda x: x[1]))
# [('b', 3), ('d', 3), ('e', 4), ('c', 5), ('a', 5)] ✅ value 값 순서로 정렬
print(sorted(my_dict.items(), key=lambda x: -x[1]))
# [('c', 5), ('a', 5), ('e', 4), ('b', 3), ('d', 3)]
print(sorted(my_dict.items(), key=lambda x: (-x[1], x[0])))
#  [('a', 5), ('c', 5), ('e', 4), ('b', 3), ('d', 3)]
~~~

# 3. 분해합
- 생성자의 범위 = 1 ~ N
- 생성자의 최소값 = N - (자리수 * 9)(각 자리수의 최대값이 9이므로)
- int('856') + map(int, '856') == int('856') + int('8') + int('5') + int('6')

# 4. 팰린드롬
## 순열
## 조합
~~~python
from itertools import permutations, combinations

nums = [1, 2, 3]
perm = permutations(nums, 2)
combi = combinations(nums, 2)

print(perm)  # 그냥 객체
print(combi)
print(list(perm))  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print(list(combi))  # [(1, 2), (1, 3), (2, 3)]

words = ['abba', 'ba', 'ababa', 'bbaa', 'baaba']

for word1, word2 in permutations(words, 2):
    p = word1 + word2

    if p == p[::-1]:
        print(p)
~~~
## N중 for문 종료
1. flag 사용해서 하나씩 break 걸기
2. exit(0)

# 5. 전기버스
- 그리디한 문제 : 현 시점에서 가장 최적의 해만 찾아나가면 최종적으로도 가장 최적의 해가 나온다
- 현 시점에서 갈 수 있는 가장 먼 곳까지 가야함
- 일단 보내고 `뒤에서부터` 확인한다
- for-else 구문 : for문이 정상적으로 돌고 끝나면 else 작동