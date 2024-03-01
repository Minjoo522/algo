for _ in range(int(input())):
    position, word = input().split()
    position = int(position)
    print(word[:position - 1] + word[position:])