# k개의 단어 중 다른 두 단어를 합침
# 회문

T = int(input())

for _ in range(T):
    k = int(input())
    words = []
    found = False
    for _ in range(k):
        words.append(input())
    for i in range(k):
        for j in range(k):
            if i == j:
                continue
            combined_word = words[i] + words[j]
            if combined_word == combined_word[::-1]:
                print(combined_word)
                found = True
                break
        if found:
            break
    if not found:
        print(0)
