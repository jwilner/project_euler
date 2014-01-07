from problem_7 import is_prime
from collections import defaultdict

target = 10
primes = [2, 3]
sums = {0: 0, 1: 0, 2: 1, 3: 1}


def prime_summations(limit):
    primes = []
    sums = defaultdict(int)

    n = 0
    while True:
        if is_prime(n):
            sums[n] += 1
            primes.append(n)

        sums[n] += sum(sums[n-k] for k in primes if k <= n / 2)
        print sums
        if n == 7:
            print [(n-k, sums[n-k]) for k in primes if k <= n / 2]
        if sums[n] >= limit:
            return n
        n += 1


if __name__ == '__main__':
    print prime_summations(8)


# we can return all numbers which:
    # 1) are equal to a previous sum + a prime
    # 2) are equal to a previous sum * a coefficient
         # + a previous sum * a coefficient

    # But all primes will be previous sums,
    # therefore we should only consider * 2

# will returning all numbers for whom
