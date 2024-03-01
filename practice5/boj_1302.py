"""
가장 많이 팔린 책의 제목
딕셔너리
"""
from collections import defaultdict

books = defaultdict(int)  # value의 디폴트 값은 0

for _ in range(int(input())):
    books[input()] += 1

book_names = sorted(books)

cnt = -1
ans = ''

for book_name in book_names:
    if books[book_name] > cnt:
        cnt = books[book_name]
        ans = book_name

print(ans)