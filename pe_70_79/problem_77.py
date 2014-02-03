from problem_7 import is_prime

def prime_summations(n):
    '''
    problem 77
    '''
    prime_sums, primes = {0:1,1:0}, []
    for i in range(2,n):
        if is_prime(i):
            primes.append(i)

    return prime_sums
