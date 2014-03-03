

def max_collatz(maximum):
    lengths = {1: 1}

    def get_collatz(n):
        seq = []
        while n not in lengths:
            seq.append(n)
            n = n // 2 if n % 2 == 0 else (n * 3) + 1

        length = lengths[n] + 1
        lengths.update({k: length + i
                        for i, k in enumerate(seq[::-1])})

    max_length = lengths[1], 1
    for x in xrange(2, maximum):
        if x not in lengths:
            get_collatz(x)
        if lengths[x] > max_length[0]:
            max_length = lengths[x], x

    return max_length


if __name__ == '__main__':
    import timeit
    print timeit.timeit("print max_collatz(10**6)",
                        setup="from __main__ import max_collatz",
                        number=10) / 10
