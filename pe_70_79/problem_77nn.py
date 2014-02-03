from prime_test import is_prime


#def prime_sums(limit):
    #current = 1
    #primes = []
    #sums = [1, 0]  # 1 way to sum to 2

    #while sums[current] < limit:
        #current += 1
        #sums.append(0)
        #if is_prime(current):
            #primes.append(current)
        #for prime in primes:
            #for j in xrange(prime, current + 1):
                #sums[j] += sums[j - prime]

    #return sums


def prime_sums(limit):

    primes = [2]
    cache = {(2, 0): 1}

    def num_prime_sums(n, prime_index):
        if (n, prime_index) in cache:
            return cache[n, prime_index]
        if prime_index < 0:
            return 0
        if n < primes[prime_index]:
            return num_prime_sums(n, prime_index - 1)
        if n == primes[prime_index]:
            return 1 + num_prime_sums(n, prime_index - 1)
        return num_prime_sums(n - primes[prime_index], prime_index) + \
            num_prime_sums(n, prime_index - 1)

    n = 2
    last_result = 1
    while last_result < limit:
        n += 1

        if is_prime(n):
            primes.append(n)

        index = len(primes) - 1
        last_result = cache[n, index] = num_prime_sums(n, index)

    return n

if __name__ == '__main__':
    print prime_sums(5000)
