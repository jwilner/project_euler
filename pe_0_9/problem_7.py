import math

def is_prime(n):
    '''
    test whether a number is prime or not
    problem 7, among others
    from notes on problem 7
    '''
    if type(n) != int:
        raise TypeError
    if n <= 1:
        return False
    if n < 4: ## {2,3}
        return True
    if n % 2 == 0:
        return False
    if n < 9: ## {5,7}
        return True
    if n % 3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(n)) ##r*r = n
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
    return True
