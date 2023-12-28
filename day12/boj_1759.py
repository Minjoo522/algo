# 조합 모듈
# 최소 한 개의 모음
# 최소 두 개의 자음
# 모음 : v개
# 자금 : L-v개
# 모음의 범위 : 1 ~ L-2(자음을 최소 2개는 뽑아야 하기 때문에)
# 자음의 범위 : 2 ~ L-1(모음을 최소 1개는 뽑아야 하기 때문에)
from itertools import combinations

vowel_gather = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, input().split())

letters = list(input().split())

vowels = []
consonants = []

for letter in letters:
    if letter in vowel_gather:
        vowels.append(letter)
    else:
        consonants.append(letter)

passwords = []

for c in range(2, L):
    for consonant in combinations(consonants, c):
        for vowel in combinations(vowels, L-c):
            tmp_password = sorted(list(vowel + consonant))
            passwords.append(tmp_password)

passwords.sort()

for password in passwords:
    print(''.join(password))