from problem_10 import get_all_primes_under


primes = get_all_primes_under(10**5)


def get_square_prime_remainder(p, n):
    return ((p - 1)**n + (p + 1)**n) % p**2


def prime_square_remainder(limit):
    for i, prime in enumerate(primes):
        r = get_square_prime_remainder(prime, i)
        if r > limit:
            return i


if __name__ == '__main__':
    print prime_square_remainder(10**9)
