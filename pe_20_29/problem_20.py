from operator import mul, add
from functools import reduce


def factorial(n):
    return reduce(mul, range(1, n))


def get_digits(n):
    while n:
        n, r = divmod(n, 10)
        yield r


def sum(seq):
    return reduce(add, seq)


def factorial_sum(n):
    return sum(get_digits(factorial(n)))


if __name__ == '__main__':
    print factorial_sum(100)
