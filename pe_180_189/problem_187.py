from problem_10 import get_all_primes_under


def number_of_prime_factors(maximum):
    primes = get_all_primes_under(maximum // 2)
    count = 0
    last_index = len(primes) - 1
    for i, p in enumerate(primes):
        while primes[last_index] * p > maximum:
            if i > last_index:
                return count  # square of prime at i still be in bounds
            last_index -= 1
        count += last_index - i + 1

if __name__ == '__main__':
    import sys
    print number_of_prime_factors(int(sys.argv[1]))
