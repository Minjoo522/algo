"""
조합
모음을 n개 뽑으면 자음은 L-n
모음(a, e, i, o, u) : 최소 1개
자음 : 최소 2개
"""
import sys
input = sys.stdin.readline

from itertools import combinations

vowels_standard = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, input().split())
letters = list(input().split())

vowels = []
consonants = []

for letter in letters:
    if letter in vowels_standard:
        vowels.append(letter)
    else:
        consonants.append(letter)

passwords = []

for v in range(1, L-1):  # L이 4면 모음은 1개 ~ 2개
    for vowel in combinations(vowels, v):
        for consonant in combinations(consonants, L-v):
            tmp = sorted(list(vowel + consonant))
            passwords.append(tmp)

passwords.sort()

for password in passwords:
    print(''.join(password))
