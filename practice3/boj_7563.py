N = int(input())
builds = [tuple(map(int, input().split())) for _ in range(N)]
result = []

for i in range(N):
    standard = builds[i]
    cnt = 1
    for build in builds:
        if standard == build:
            continue
        if standard[0] < build[0] and standard[1] < build[1]:
            cnt += 1
    result.append(cnt)

print(*result)