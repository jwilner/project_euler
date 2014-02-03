import itertools
from problem_7 import is_prime

def pandigital_prime(num_digits = 4):
    '''
    find largest number that uses all digits 1 through num_digits and is prime
    problem 41
    '''
    for num_d in range(num_digits,0,-1):
        digits = [str(d) for d in range(1,num_d+1)]
        perms = itertools.permutations(''.join(reversed(digits)))
        for i in perms:
            num = int(''.join(i))
            if is_prime(num): return num
