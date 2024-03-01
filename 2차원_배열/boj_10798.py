import sys

input = sys.stdin.readline

words = [input().rstrip() for _ in range(5)]
max_length = max(len(word) for word in words)

board = [["" for _ in range(max_length)] for _ in range(5)]

for index, word in enumerate(words):
    board[index][:len(word)] = list(word)

result = ""
for x in range(max_length):
    for y in range(5):
        result += board[y][x]

print(result)
