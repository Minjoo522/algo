"""
이차원 리스트

- 1시간마다 이동
- 약품 구역 : 미생물의 절반이 죽고, 이동방향이 반대로
    - 숫자 및 방향 변경
- 두 개 이상의 군집이 한 셀에 모이는 경우 = 군집들이 합쳐진다
    - 이동방향 : 미생물 수가 많은 군집의 이동방향

- M 시간 : M번 이동
- 매 시간 K개의 군집이 어떻게 움직이는지 검토

남아 있는 미생물의 수
"""
from collections import defaultdict

dr = [0, -1, 1, 0, 0]  # (1: 상, 2: 하, 3: 좌. 4: 우)
dc = [0, 0, 0, -1, 1]
rev = [0, 2, 1, 4, 3]  # 반대 방향

for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    germs = [list(map(int, input().split())) for _ in range(K)]

    for _ in range(M):
        merge_check = defaultdict(list)  # 매 시간마다 합체 여부 판단할 딕셔너리

        for i in range(K):
            r, c, n, d = germs[i]

            if not n:  # 합쳐졌거나 소멸하여 숫자가 0인 군집은 건너뛰기
                continue

            nr, nc = r + dr[d], c + dc[d]

            if nr in [0, N - 1] or nc in [0, N - 1]:  # 위치가 모서리
                n //= 2
                d = rev[d]

            germs[i] = [nr, nc, n, d]  # 군집 정보 갱신
            merge_check[(nr, nc)].append((i, n, d))  # 합체 여부 확인 : 딕셔너리에 추가 (nr, nc): [(군집 번호, 몇 마리, 이동 방향)]

        for j in merge_check.values():
            if len(j) > 1:  # 두 군집 이상이 같은 위치에 존재
                cnt = 0
                max_i, max_n = -1, -1
                for i, n, d in j:  # 최대 군집의 번호 및 숫자로 갱신
                    cnt += n  # 각 군집의 마리수 합치기
                    if n > max_n:
                        max_i = i  # 제일 많은 애의 인덱스 번호
                        max_n = n
                germs[max_i][2] = cnt

                for i, n, d in j:
                    if i != max_i:
                        germs[i][2] = 0  # 나머지 군집의 숫자는 모두 0으로 초기화(if not n: 여기서 걸러짐)

    ans = 0
    for r, c, n, d in germs:
        ans += n

    print(f'#${tc} {ans}')
