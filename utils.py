import itertools

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

