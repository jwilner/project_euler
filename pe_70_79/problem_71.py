from fractions import Fraction
import bisect

def proper_reduced_fraction_to_left(target='3/7',d_max=8):
    '''
    find the reduced proper fraction directly
    to the left of the given target
    problem 71
    '''

    target = Fraction(target)
    frac_list = [target]
    targ_index = 0

    multiplier = (d_max-target.denominator)//target.denominator
    n,d = target.numerator*multiplier,target.denominator*multiplier
    if not multiplier:
        n,d = 0,1

    while d < d_max:
        while n/d < target:
            n += 1
        n -= 1
        f = Fraction(n,d)
        i = bisect.bisect(frac_list,f)
        if i == targ_index:
            frac_list.insert(i,f)
            n,d,targ_index = n+1,d+1,targ_index+1
            continue
        n,d = n+1,d+1
    return frac_list[targ_index-1]

def fraction_cheating(n=3,d=7,limit = 1000000):
    '''
    find the reduced proper fraction directly
    to the left of the given target
    problem 71
    '''
    real = Fraction(n,d)
    approx = Fraction(n/d)
    while approx.limit_denominator(limit) == real: #Fraction(7720456504063707, 18014398509481984)
        approx = Fraction(approx.numerator-1,approx.denominator)
    return approx #Fraction(3595117, 8388608)???
