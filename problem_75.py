from utils import solve_quadratic
from fractions import gcd

def singular_integer_right_triangles(limit=1500000):
    '''
    problem 75
    '''
    def has_triple(p):
        m_max = int(p**.5)
        m_min = int(max(solve_quadratic(2,-1,-p)))
        for m in range(m_min,m_max+1):
            for n in range(1 if m % 2 == 0 else 2,m,2):
                if gcd(m,n) > 1: continue
                if m*(m+n) == p: return 1
        return 0

    internal_limit = int(limit/2)+1
    perimeters = {p:0 for p in range(5,internal_limit)}
    for p,num in perimeters.items():
        if num != 0:
            continue
        if has_triple(p):
            for x in range(p,internal_limit,p): perimeters[x] = 1 if perimeters[x] == 0 else -1
    return perimeters

def singular_pythagorean_triple(limit = 1500000):
    '''
    problem 75
    '''
    internal_limit = int(limit/2)
    perimeters = [0]*internal_limit
    for m in range(2,int(internal_limit**.5)+1):
        for n in range(1 if m % 2 == 0 else 2,m,2):
            if gcd(m,n) == 1:
                p = m*(m+n)
                for x in range(p,internal_limit,p): perimeters[x] += 1
    return perimeters.count(1)

def coprime_pair_generator(maximum):
    last_coprimes = {(2,1)}
    while last_coprimes:
        new_coprimes = set()
        for a,b in last_coprimes:
            yield (a,b)
            new_coprimes.update((c,d) for c,d in ((2*a-b,a),(2*a+b,a),(a+2*b,b)) if c < maximum)
        last_coprimes = new_coprimes

def pythagorean_triples(limit = 1500000):
    '''
    problem 75
    '''
    internal_limit = int(limit/2)
    perimeters = [0]*internal_limit
    for m,n in coprime_pair_generator(internal_limit**.5):
        p = m*(m+n)
        for x in range(p,internal_limit,p): perimeters[x] += 1
    return perimeters.count(1)

def final_test(limit = 1500000):
    internal_limit = int(limit/2)
    perimeters = [0]*internal_limit
    m_max = internal_limit**.5
    def branch(m, n):
        if m < m_max:
            p = m*(m+n)
            for x in range(p,internal_limit,p): perimeters[x] += 1
            branch(2*m - n, m)
            branch(2*m + n, m)
            branch(m + 2*n, n)
    branch(2, 1)
    return perimeters.count(1)
