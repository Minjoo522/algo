# 앞, 뒤 조사
# 문자 순회하며

N = int(input())
count = 0


def checker(word):
    word_list = [word[0]]

    for i in range(1, len(word)):
        if word[i - 1] != word[i]:
            word_list.append(word[i])

    word_set = set(word_list)
    return len(word_list) == len(word_set)


for _ in range(N):
    if checker(input()):
        count += 1

print(count)