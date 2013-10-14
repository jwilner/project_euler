
def find_digit_cancelling_fractions(num_digits):
	'''
	find those fractions, which, like 49/98, have a digit on both
	the top and bottom which can be eliminated while preserving the value.
	problem 33
	'''
	range_start,range_end = 10**(num_digits-1),10**num_digits
	numerators, denominators = range(range_start,range_end),range(range_start,range_end)
	all_possible_fractions =  [(n,d,set(n),set(d)) for (n,d) in [(str(n),str(d)) for (n,d) in itertools.product(numerators,denominators) if n < d and n % 11 != 0 and d % 11 != 0 and n % 10 != 0 and d % 10 != 0]]
	intersecting_fractions = [(n,d,''.join(intersect)) for (n,d,intersect) in [(n,d,n_set.intersection(d_set)) for (n,d,n_set,d_set) in all_possible_fractions if n_set != d_set] if intersect]
	return [(n,d) for (n,d,n1,d1) in [(int(n),int(d),int(n.replace(i,'')),int(d.replace(i,''))) for (n,d,i) in intersecting_fractions] if n/d == n1/d1]


