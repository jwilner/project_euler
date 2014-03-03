

def get_digits(n):
    while n:
        n, r = divmod(n, 10)
        yield r


def sum_of_digits(n):
    return sum(get_digits(n))

if __name__ == '__main__':
    print sum_of_digits(int("1" + "0" * 1000, 2))