# stack, queue에 중복해서 들어가지 않도록 하기
- stack, queue에 넣을 때 즉시 방문 체크를 같이 해 줌

# deque
- pop(0) ❌
~~~python
from collections import deque  # pop(0) 대신 사용

    Q = deque()  # Q 처음 만들 때 deque() 객체 만듦
    Q.append((r, c))
    dist[r][c] = 1

    while Q:
        # curr_r, curr_c = Q.pop(0)  # 시간 초과 O(N)
        curr_r, curr_c = Q.popleft()
~~~