

def consecutive_positive_divisors(maximum):
    sieve = [0] * maximum
    count = 0
    try:
        for i in range(2, maximum):
            for j in range(i * 2, maximum, i):
                sieve[j] += 1
            if sieve[i] == sieve[i + 1]:
                count += 1
    except IndexError:
        return count

if __name__ == '__main__':
    print consecutive_positive_divisors(10 ** 7)
