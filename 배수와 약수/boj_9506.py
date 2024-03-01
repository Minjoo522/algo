import sys

input = sys.stdin.readline

while True:
    n = int(input())

    if n == -1:
        break

    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)

    sum_of_factors = sum(factors)

    if len(factors) != 0 and n == sum_of_factors:
        result = ' + '.join(map(str, factors))
        print(f"{n} = {result}")
    else:
        print(f"{n} is NOT perfect.")
