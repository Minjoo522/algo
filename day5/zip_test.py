a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b)))  # [(1, 4), (2, 5), (3, 6)]
# 세로로 묶어서 튜플로 만듦
c = [7, 8, 9]
# zip 이용하여 전치
print(list(zip(a, b, c)))  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

d = [1, 2, 3, 4]
e = [5, 6]
f = [7, 8, 9]
print(list(zip(d, e, f)))  # [(1, 5, 7), (2, 6, 8)]

matrix = [[3, 7, 9],
          [4, 2, 6],
          [8, 1, 5]]

zipped_matrix = list(zip(*matrix))  # * : unpacking 연산자 / 이차원 리스트를 풀어서 넣기
# * 안쓰면...
print(list(zip(matrix)))  # [([3, 7, 9],), ([4, 2, 6],), ([8, 1, 5],)]

# 전치 완료 후, 원소를 리스트로 활용
transposed_matrix = list(map(list, zip(*matrix)))
print(transposed_matrix)  # [[3, 4, 8], [7, 2, 1], [9, 6, 5]]
