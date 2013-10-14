import math,itertools


def getProperDivisors(n):
	'''
	this function returns all the proper divisors
	for any given number(e.g. 6: {1,2,3})
	problem23
	'''
	limit = math.floor(math.sqrt(n))
	i = 2
	factors = {1}
	while i <= limit:
		if n % i == 0:
			factors.update([i, n // i])
		i += 1
	return tuple(factors)

def getNonSumOfAbundantNumbers(max):
	'''
	takes a max and returns a list of all numbers not equal
	to the sum of any two abundant numbers
	problem23
	'''
	abundant = []
	i = 0
	while i < max:
		i += 1
		factors = getProperDivisors(i)
		if sum(factors) > i:
			abundant.append(i)

	pairs = itertools.product(abundant,abundant)

	sieve = {d:0 for d in range(1,max+1)}
	for p in pairs:
		paired = sum(p)
		if paired <= max:
			sieve[paired] = 1
	return [i for (i,val) in sieve.items() if val == 0]


