# 해쉬 자료 구조
- `hashable` : 고유값으로 특정할 수 있는!
- 딕셔너리, set
- 공간(메모리)을 많이 잡아 먹는 대신, 조회가 빠르다.

# set
- 생성자 : set()
- 리터럴로 생성 불가
- 집합
- a & b : 교집합
- a | b : 합집합
- 숫자, 문자, `튜플` : 딕셔너리의 key 값이 될 수 있는 자료형과 일치
- ***순서를 보장하지 않음***
### .add()
- set 자료 구조 안에 set, list, dictionary 넣기 불가
- 튜플은 가능!

# dictionary
- `key는 고유`해야 한다
### .get(키 값, 없으면 반환할 값 지정)
~~~python
votes = {}

# 아래는 key 없으면 바로 keyError
# if votes['minjoo']:
#     votes['minjoo'] += 1

# get 메서드 이용!
if votes.get('minjoo', -1) == -1:
    votes['minjoo'] = 0
else:
    votes['minjoo'] += 1
~~~
### .pop(key, 없으면 반환할 값)
- del은 key 값이 없으면 에러 발생
~~~python
dict2 = {'name': 'jane', 'age': 7, 'license': True}
del dict2['name']
~~~

# 스트링
### .split()
~~~python
a = '1234'
list(a)  # ['1', '2', '3', '4']
~~~