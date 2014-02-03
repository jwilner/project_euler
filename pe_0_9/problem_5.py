from collections import defaultdict


def factorize(n):
    factors = defaultdict(int)
    for f in range(2, int(n ** 5)):
        while n % f == 0:
            factors[f] += 1
            n /= f
        if n == 1:
            break
    return factors


def smallest_multiple(arr):
    factorized = [factorize(v) for v in arr]
    necessary = ((v, max(f[v] for f in factorized)) for v in arr)

    result = 1
    for value, freq in necessary:
        result *= value ** freq
    return result


if __name__ == '__main__':
    print smallest_multiple(range(1, 20))
