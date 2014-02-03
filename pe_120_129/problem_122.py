

def minimum_exponent(n, target, exponents=set()):
    if n == target:
        return 0
    remaining = target - n
    exponents.add(n)
    return min(1 + minimum_exponent(n + v, target, exponents.copy())
               for v in exponents if v <= remaining)


if __name__ == '__main__':
    for i in range(2, 40):
        print i, minimum_exponent(1, i)
