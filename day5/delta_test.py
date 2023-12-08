r = c = 1  # 중간에 있다고 가정
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
# 하, 상, 좌, 우

for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    print(nr, nc)