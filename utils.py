import itertools,functools

def nth(iterable, n, default=None):
    '''
    Returns the nth item or a default value
    '''
    return next(itertools.islice(iterable, n, None), default)


def factors(n):
    return set(functools.reduce([1].__add__,([i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)))

def solve_quadratic(a,b,c):
    '''
    uses determinant and quadratic formula to return roots given
    coefficients
    '''
    d = (b**2)-(4*a*c)
    if d < 0:
        return tuple()
    if d == 0:
        return tuple([(-b)/(2*a)])
    else:
        rooted = d**.5
        return ((-b+rooted)/(2*a),(-b-rooted)/(2*a))

def pollard_brent(n):
    '''
    implementation of pollard brent algorithm for finding a prime factor of n
    https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/
    '''
    if n % 2 == 0: return 2
    if n % 3 == 0: return 3
    y, c, m = random.randint(1, n-1), random.randint(1, n-1), random.randint(1, n-1)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range(r):
            y = (pow(y, 2, n) + c) % n
        k = 0
        while k < r and g==1:
            ys = y
            for i in range(min(m, r-k)):
                y = (pow(y, 2, n) + c) % n
                q = q * abs(x-y) % n
            g = fractions.gcd(q, n)
            k += m
        r *= 2
    if g == n:
        while True:
            ys = (pow(ys, 2, n) + c) % n
            g = fractions.gcd(abs(x - ys), n)
            if g > 1:
                break
    return g


small_primes = get_all_primes_under(1000)
def prime_factors(n):
    '''
    prime factorization employing pollarrd brent algorithm
    http://stackoverflow.com/questions/4643647/fast-prime-factorization-module
    '''
    factors = []

    limit = int(n ** .5) + 1
    for checker in small_primes:
        if checker > limit: break
        while n % checker == 0:
            factors.append(checker)
            n //= checker
            limit = int(n ** .5) + 1
        if checker > limit: break

    if n < 2: return factors

    while n > 1:
        if is_prime(n):
            factors.append(n)
            break
        factor = pollard_brent(n) # trial division did not fully factor, switch to pollard-brent
        factors.extend(prime_factors(factor)) # recurse to factor the not necessarily prime factor returned by pollard-brent
        n //= factor
    return factors

class Totient:
    def __init__(self, n):
        self.totients = [1 for i in range(n)]
        for i in range(2, n):
            if self.totients[i] == 1: #then prime b/c not yet hit by later steps a la sieve
                for j in range(i, n, i): #every multiple of i less than n
                    self.totients[j] *= i - 1 #increase each multiple's number of totients by factor (i-1), b/c every prime p has phi(p) == p-1
                    k = j / i # k is another integer (b/c corresponds to iteration) factor of j
                    while k % i == 0: #if k has powers of i in it
                        self.totients[j] *= i
                        k /= i
    def __call__(self, i):
        return self.totients[i]

def totient(n):
    return int(n * functools.reduce(operator.mul,[1-fractions.Fraction(1,i)  for i in set(prime_factors(n))]))

def dijkstra(graph,source,target,neighbor_func,distance_func):
    infinity = float('inf')
    unvisited,distances,previous = {n for n in graph},collections.defaultdict(lambda : infinity),collections.defaultdict(lambda : None)
    distances[source] = 0
    while unvisited:
        current = min(unvisited.intersection(distances),key=lambda x:distances[x])
        unvisited.remove(current)
        if distances[current] == infinity:
            break
        for n in neighbor_func(current):
            if n not in unvisited:
                continue
            alt = distances[current] + distance_func(current,n)
            if alt < distances[n]:
                distances[n],previous[n] = alt, current
    if not target:
        return previous
    s,u = [],target
    while previous[u]:
        s.append(u)
        u = previous[u]
    s.reverse()
    return tuple([source]+s)
