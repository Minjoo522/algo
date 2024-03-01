import sys

input = sys.stdin.readline

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input().rstrip()

for c in croatia:
    word = word.replace(c, "*")

print(len(word))
