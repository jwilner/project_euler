import math

def get_all_primes_under(maximum):
    '''
    returns list of all primes under maximum ('sieve of eratosthones')
    problem 10, problem 27
    '''
    boundary = math.floor((maximum - 1) / 2) ##only odds need be considered
    sieve = {d:False for d in range(1,boundary+1)}
    '''
    sieve index i corresponds to odd number 2i + 1
    '''

    cross_limit = (math.floor(math.sqrt(maximum)) -1) / 2
    '''
    only need to look for primes as far as square root of maximum
    '''
    i = 1
    while i <= cross_limit:
        if not sieve[i]: ##then 2i + 1 prime
            for j in range(2*i*(i+1),boundary+1,(2*i)+1):
                sieve[j] = True
        i += 1
        '''
        If i is false, then 2i+i is prime, and all multiples of 2i+i
        less than (2i+1)^2 will have already been marked non-prime
        (as multiples of numbers less than 2i + 1); index of (2i+1)^2
        is 2i*(i+1); start at that index, and
        '''
    return [2]+[2*i+1 for (i,v) in sieve.items() if v == False]
