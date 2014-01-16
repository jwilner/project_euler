

def largest_prime_factor(n):
    '''Because only generating actual primes is too taxing, and any factors
    that you encounter after factoring out all earlier ones will necessarily
    be prime'''
    for p in [2] + range(3, int(n**.5), 2):
        while n % p == 0:
            n /= p
        if n == 1:
            return p
    return n


if __name__ == '__main__':
    print largest_prime_factor(600851475143)
