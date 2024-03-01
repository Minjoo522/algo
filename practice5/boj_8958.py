"""
연속된 O의 개수
"""
for _ in range(int(input())):
    total = 0
    current = 0

    for result in input():
        if result == 'O':
            current += 1
            total += current
        elif result == 'X':
            current = 0

    print(total)