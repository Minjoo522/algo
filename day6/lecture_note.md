# 주의
- 변수명 : 내장함수, 내장 메서드 사용 x (count, sum, max ...)

# 파리 퇴치
- 검토 범위 설정
- (0, 0)을 기준으로 시작
- M * M을 확인해 나가면서 max 값 갱신
- 끝 열, 행은 검토하지 않음(M * M에 포함되기 때문에) ➡️ N - M + 1
## 4중 for문
~~~python
for r in range(N - M + 1):
    for c in range(N - M + 1):
        tmp = 0
        for i in range(r, r + M):
            for j in range(c, c + M):
                tmp += board[i][j]
~~~
## for문 한 줄 작성
~~~python
tmp = sum(board[y][x] for y in range(r, r+M) for x in range(c, c+M))
~~~

# 풍선팡2
- 상하좌우 : 델타 탐색
- 델타 탐색 세팅 : 맨 위에 해 놓기!(반복 문 위)
  - ❓: 반복문 돌 때마다 새로 세팅하지 않도록
- 전부 검색해야 함
- 주어진 범위 벗어나지 않도록 주의!(인덱스 에러 주의)
  1. 조건 걸기
  2. 2차원 리스트 패딩 = 리스트 한 겹 감싸주기
     ~~~python
     # 틀 짜기
     board = [[0 for _ in range(M + 2)] for _ in range(N + 2)]
     # 입력 받아서 갖다 붙이기
     for i in range(1, N + 1):
        board[i][1:M+1] = map(int, input().split())
     # 기준 잡고 델타 탐색
     for r in range(1, N + 1):
        for c in range(1, M + 1):
            cnt = board[r][c]
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                cnt += board[nr][nc]
     ~~~
     
# 이진 탐색
- 탐색지가 타겟보다 `크다` : `오른쪽` 갱신
- 탐색지가 타겟보다 `작다` : `왼쪽` 갱신

1. while
2. 재귀