from problem_7 import is_prime

def spiral_prime_ratio(i = 10):
    '''
    find the first ring of spiral prime at which the ratio of primes
    is less than given %
    problem 58
    '''

    percent = 100/i
    primes = 0
    corners = 1
    for i in range(2,10**6,2):
        side = i+1
        square = side**2
        primes += len([c for c in range(1,4) if is_prime(square-(c*i))])
        corners += 4
        if percent*primes < corners:
            return (side,primes,corners)
