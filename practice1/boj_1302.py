N = int(input())
books = {}
for _ in range(N):
    title = input()
    if books.get(title):
        books[title] += 1
    else:
        books[title] = 1
max_value = max(books.values())
max_titles = [title for title, value in books.items() if value == max_value]
print(sorted(max_titles)[0])
