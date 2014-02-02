

def is_prime(n):
    if n < 2:
        return False

    max_factor = n**.5

    def seq_gen():
        for f in 2, 3:
            yield f

        k = 6
        while True:
            for f in k - 1, k + 1:
                yield f
            k += 6

    for f in seq_gen():
        if f > max_factor:
            return True
        if n % f == 0:
            return False
