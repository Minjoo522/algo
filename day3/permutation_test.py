from itertools import permutations, combinations

nums = [1, 2, 3]
perm = permutations(nums, 2)
combi = combinations(nums, 2)

print(perm)  # 그냥 객체
print(combi)
print(list(perm))  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print(list(combi))  # [(1, 2), (1, 3), (2, 3)]

words = ['abba', 'ba', 'ababa', 'bbaa', 'baaba']

for word1, word2 in permutations(words, 2):
    p = word1 + word2

    if p == p[::-1]:
        print(p)
