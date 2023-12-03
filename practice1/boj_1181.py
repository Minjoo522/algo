# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다. == set 사용

# sorted_data = sorted(data, key=lambda x: (len(x), x))

N = int(input())
words = [input() for _ in range(N)]

sorted_words = sorted(set(words), key=lambda word: (len(word), word))

print('\n'.join(sorted_words))
