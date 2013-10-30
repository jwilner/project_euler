import math

def find_lowest_possible_integer(i,test):
    '''
    apply test to every integer equal to and greater than i, and return the first integer for which the test evaluates true
    '''
    if not hasattr(test, '__call__'):
        raise TypeError

    while not test(i):
        i += 1

    return i

def combinations_over(n_min = 22,n_max = 101,maximum = 1000000):
    '''
    find every nCr number of combinations greater than n for the given possible range of n
    problem 53
    '''
    combinations = {}
    for n in range(n_min+1,n_max):
        found = {}
        r = math.ceil(n/2)
        while r > 0:
            ncr = (math.factorial(n)) / (math.factorial(r)*(math.factorial(n-r)))
            if ncr <= maximum:
                break
            found[(n,r)] = ncr
            r -= 1
        found.update({(n,n-r):ncr for ((n,r),ncr) in found.items() if n-r != r})
        combinations.update(found)
    return combinations
