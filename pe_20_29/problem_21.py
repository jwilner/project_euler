from collections import defaultdict


def proper_divisors(n):
    """Why do I sort? Because I can."""
    bigger = []
    yield 1
    for i in range(2, int(n ** .5)):
        if n % i == 0:
            yield i
            bigger.append(n // i)
    while bigger:
        yield bigger.pop()


def find_all_amicable_numbers_under(maximum):
    freq_dict = defaultdict(int)
    for pair in ((n, sum(proper_divisors(n))) for n in xrange(1, maximum)):
        freq_dict[tuple(sorted(pair))] += 1

    return sum(sum(nums) for nums, freq in freq_dict.items() if freq > 1)


if __name__ == '__main__':
    print find_all_amicable_numbers_under(10000)
