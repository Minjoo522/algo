import sys

input = sys.stdin.readline

word = input().rstrip()
alphabet_in_word = []

for char in range(ord('a'), ord('z') + 1):
    alphabet = chr(char)
    if alphabet in word:
        alphabet_in_word.append(word.index(alphabet))
    else:
        alphabet_in_word.append(-1)

print(*alphabet_in_word)

"""
import sys
alphabet = 'abcdefghijklmnopqrstuvwxyz'
s = sys.stdin.readline()
mylist =[]

for i in range(len(alphabet)):
    if alphabet[i] in s:
        mylist.append(s.index(alphabet[i]))
    elif alphabet[i] not in s:
        mylist.append(-1)

print(*mylist)
"""