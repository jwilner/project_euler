from fractions import Fraction

def convergent_of_e(n):
    '''
    returns the nth convergent of the continued fraction of e
    problem 65
    '''
    n -= 1
    convergent_points = []#collections.deque()
    for i in range(1,n+1):
        if (i - 2) % 3 == 0:
            convergent_points.append(int(2*(i+1)/3))
        else:
            convergent_points.append(1)
    conv = 0
    while convergent_points:
        conv = Fraction(1/(convergent_points.pop() + conv))
    return Fraction(2+conv)

def n_convergents_of_root_two(i):
    '''
    returns the nth convergent of the continued fraction of root two
    problem 65
    '''
    n,d = 1,1
    fracs = []
    for j in range(0,i):
        n,d = n+d+d,n+d
        fracs.append(Fraction(n,d))
    return fracs
