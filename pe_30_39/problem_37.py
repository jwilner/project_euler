from problem_7 import is_prime


def truncatable_primes(maximum = 1000000):
    '''
    find all eleven 'truncatable' primes
    problem 37
    '''
    poss_digits = set('1379')
    all_primes = get_all_primes_under(maximum)
    poss_primes = [p for p in [str(p) for p in all_primes] if set(p[1:]) <= poss_digits]
    #primes can only be composed of the digits 1,3,7, and 9
    #after the first digit

    final_primes = []
    for p in poss_primes:
        found = True
        length = len(p)
        for i in range(0,length):
            if not is_prime(int(p[i:])) or not is_prime(int(p[:i+1])):
                found = False
                break
        if found: final_primes.append(int(p))
    return final_primes
