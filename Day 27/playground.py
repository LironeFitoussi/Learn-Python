def add(*arg):
    sum1 = 0
    for n in arg:
        print(n)
        sum1 += n
    print(sum1)
    return sum(arg)


print(add(1, 2, 3, 4, 5))  # 15


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)  # 25
