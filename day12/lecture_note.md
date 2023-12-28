# N과 M(5)
## DFS
- 정점이 N개인 무방향 완전 그래프를 M번 깊이까지 DFS 탐색할 수 있는 경우의 수
- depth가 M이 되면 출력
- DFS : 탐색과 동시에 방문이 이루어짐
~~~python
def perm(depth):
    if depth == M:
        print(*ans)
        return

    for num in nums:
        if num not in visited:
            visited.add(num)
            ans.append(num)
            perm(depth + 1)
            ans.pop()
            visited.discard(num)


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = set()
ans = []

perm(0)
~~~

# N과 M(6)
## DFS
- 유방향 비순환 그래프(높은 숫자는 낮은 숫자를 방문할 수 없다)

~~~python
def combination(idx, depth):
    if depth == M:
        print(*ans)
        return

    for i in range(idx, N):
        if i not in visited:
            visited.add(i)
            ans.append(nums[i])
            combination(i + 1, depth + 1)
            ans.pop()
            visited.discard(i)


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = set()
ans = []

combination(0, 0)
~~~

# 최적경로
- N개의 방문지 가운데 N개를 뽑아 순서를 결정하는 문제 ➡️ 순열
- N개의 정점을 이어진 경로로 완전 탐색하는 문제 ➡️ DFS
## DFS, 순열
~~~python
from collections import deque


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def dfs(now, distance, depth):
    global ans

    # N개의 방문지를 모두 돌았을 때
    if depth == N:
        distance += dist(now, end)
        ans = min(distance, ans)
        return

    # 백트래킹 : 중간 거리가 현재 정답보다 크다면 리턴(유망하지 않은 경로 더 이상 탐색하지 않음)
    if distance > ans:
        return

    # 탐색할 곳이 남았고 아직 유망한 경로 탐색
    for after in range(N):
        if not visited[after]:
            visited[after] = 1
            dfs(house[after], distance + dist(now, house[after]), depth + 1)
            visited[after] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    coordinates = deque(list(map(int, input().split())))

    start = [coordinates.popleft(), coordinates.popleft()]
    end = [coordinates.popleft(), coordinates.popleft()]
    house = []
    for _ in range(N):
        house.append([coordinates.popleft(), coordinates.popleft()])

        ans = 987654321
        visited = [0] * N

        dfs(start, 0, 0)

        print(f'{tc} {ans}')
~~~

# 외판원 순회
~~~python
# 임의의 위치에서 시작
# 시작 위치로 되돌아 갈 것

def dfs(now, cost, depth):
    global ans

    if depth == N:  # 시작점으로 돌아갈 수 있으면 정답 갱신
        if cost_matrix[now][0]:
            cost += cost_matrix[now][0]
            ans = min(ans, cost)
            return
    else:  # 길이 없다면 더 이상 탐색하면 안됨
        return

    # 백트래킹
    if cost > ans:
        return

    for after in range(N):
        if not visited[after] and cost_matrix[now][after]:
            visited[after] = 1
            dfs(after, cost + cost_matrix[now][after], depth + 1)
            visited[after] = 0


N = int(input())
cost_matrix = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * N
ans = 987654321

visited[0] = 1
dfs(0, 0, 1)  # 진짜 dfs의 시작은 1번 depth부터

print(ans)
~~~

# 비트마스킹으로 방문지 표시하기
~~~python
# 방문 표시
# 방문 확인

def dfs(now, cost, depth, visited):
    global ans

    if depth == N:  # 시작점으로 돌아갈 수 있으면 정답 갱신
        if cost_matrix[now][0]:
            cost += cost_matrix[now][0]
            ans = min(ans, cost)
            return
    else:  # 길이 없다면 더 이상 탐색하면 안됨
        return

    # 백트래킹
    if cost > ans:
        return

    for after in range(N):
        if not cost_matrix[now][after] or visited & (1 << after):
            # 방문 확인
            # & 연산만 다름
            continue

        dfs(after, cost+cost_matrix[now][after], depth+1, visited | (1 << after))
        # 방문 표시
        # or 연산 특성상 이미 방문한 곳은 1, shift한 자리 수는 1로 바뀜


N = int(input())
cost_matrix = [list(map(int, input().split())) for _ in range(N)]

ans = 987654321

dfs(0, 0, 1, 1)

print(ans)
~~~

# 암호 만들기
~~~python
# 조합 모듈
# 최소 한 개의 모음
# 최소 두 개의 자음
# 모음 : v개
# 자금 : L-v개
# 모음의 범위 : 1 ~ L-2(자음을 최소 2개는 뽑아야 하기 때문에)
# 자음의 범위 : 2 ~ L-1(모음을 최소 1개는 뽑아야 하기 때문에)
from itertools import combinations

vowel_gather = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, input().split())

letters = list(input().split())

vowels = []
consonants = []

for letter in letters:
    if letter in vowel_gather:
        vowels.append(letter)
    else:
        consonants.append(letter)

passwords = []

for c in range(2, L):
    for consonant in combinations(consonants, c):
        for vowel in combinations(vowels, L-c):
            tmp_password = sorted(list(vowel + consonant))
            passwords.append(tmp_password)

passwords.sort()

for password in passwords:
    print(''.join(password))
~~~