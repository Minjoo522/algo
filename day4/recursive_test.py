def func(n):
    if n == 3:
        return

    print(f'{n}의 세상에 옴')
    func(n + 1)
    print(f'{n}의 세상의 마무리')


func(0)
# 0의 세상에 옴
# 1의 세상에 옴
# 2의 세상에 옴
# 2의 세상의 마무리
# 1의 세상의 마무리
# 0의 세상의 마무리
