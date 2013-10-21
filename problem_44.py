
def pentagon_gen(start = 1,end = 10000, interval = 1):
	'''
	pentagonal number generator
	'''
	n = start
	sign = 1 if interval > 0 else -1
	while n*sign < end:
		yield int((n*((3*n)-1))/2)
		n += interval

def hexagon_gen(start = 1, end = 1000, interval = 1):
	'''
	hexagonal number generator
	'''
	n = start
	sign = 1 if interval > 0 else -1
	while n*sign < end:
		yield int(n*(2*n-1))
		n += interval

def heptagon_gen(start = 1, end = 1000, interval = 1):
	'''
	heptagonal number generator
	'''
	n = start
	sign = 1 if interval > 0 else -1
	while n*sign < end:
		yield int(n*(5*n-3)/2)
		n += interval

def octagon_gen(start = 1, end = 1000, interval = 1):
	'''
	octagonal number generator
	'''
	n = start
	sign = 1 if interval > 0 else -1
	while n * sign < end:
		yield int(n*(3*n-2))
		n += interval

def triangle_gen(start = 1, end = 1000, interval = 1):
	'''
	triangular number generator
	'''
	n = start
	sign = 1 if interval > 0 else -1
	while n * sign < end:
		yield int(n*(n+1)/2)
		n += interval

def pentagonal_pairs():
	'''
	find the pair of pentagonal numbers such that P1-P2 is pentagonal, P1 + P2 is pentagonal, and the difference is minimized
	problem 44
	'''
	i = 0
	for p1 in pentagon_gen():
		i += 1
		for p2 in pentagon_gen(i,0,-1):
			if is_pentagonal_number(p1+p2) and is_pentagonal_number(p1-p2):
				return (p1,p2,p1-p2)


