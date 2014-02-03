
def is_permuted_multiple(n,iters = 6):
    '''
    return true or false if the digits of n and the digits of its multiples up to n x iters are identical
    problem 52
    '''
    n_set = set(str(n))
    for i in range(2,iters+1):
        if set(str(i*n)) != n_set:
            return False
    return True
