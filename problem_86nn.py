

maximum = 100


def is_coprime(x, y):
    while y:
        x, y = y, x % y
    return x == 1


def coprime_gen(maximum=float('inf')):
    x = 1
    while x < maximum:
        for y in range(1, x, 1 if x % 2 else 2):  # if x even then y odd
            if is_coprime(x, y):
                yield x, y
        x += 1


def pythagorean_triples(max_side=100):
    '''generate using Euclid's formula'''
    for m, n in coprime_gen(maximum=max_side ** .5):
        if (m - n) % 2 == 0:
            continue
        k = 1
        while True:
            a = k * (m ** 2 - n ** 2)
            b = 2 * k * m * n
            c = k * (m ** 2 + n ** 2)
            if c > max_side:
                break
            small, big = (a, b) if a < b else (b, a)
            yield small, big, c
            k += 1


def count_integer_solutions(target=2000):
    solutions = set()
    for a, b, _ in sorted(pythagorean_triples(10**4), key=lambda x: x[1]):
        solutions.update(tuple(sorted([new_a, a - new_a, b]))
                         for new_a in xrange(1, a))
        solutions.update(tuple(sorted([new_b, b - new_b, a]))
                         for new_b in xrange(1, b))
        if len(solutions) >= target:
            return b, solutions, len(solutions)

if __name__ == '__main__':
    print count_integer_solutions()
