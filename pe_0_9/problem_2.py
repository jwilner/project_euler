

def sum_even_fibs(limit=4*10**6):
    def fib_gen():
        a, b = 1, 1
        while b < limit:
            yield b
            a, b = b, a + b

    return sum(f for f in fib_gen() if f % 2 == 0)


if __name__ == '__main__':
    print sum_even_fibs()
