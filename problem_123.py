from problem_10 import get_all_primes_under
from itertools import islice


primes = get_all_primes_under(10**6)


def get_square_prime_remainder(p, n):
    return ((p - 1)**n + (p + 1)**n) % p**2


def prime_square_remainder(limit):
    for i, prime in islice(enumerate(primes), 7034, None, 2):
        r = get_square_prime_remainder(prime, i + 1)
        if r > limit:
            return i + 1


if __name__ == '__main__':
    print prime_square_remainder(10**10)
