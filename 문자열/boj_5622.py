"""
다이얼을 걸기 위해서 필요한 최소 시간
- 전화 번호 : 리스트의 인덱스
- 알파벳 : 리스트의 값
"""
import sys

input = sys.stdin.readline

dial = ["", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
word = input().rstrip()

time = 0

for char in word:
    for i in range(len(dial)):
        if char in dial[i]:
            time += 2 + i - 1

print(time)
