
def square_digit_chains(maximum = 10000000):
	'''
	Sequences produced by summing the squares of the digits of the last terms always end in either 1 or 89; how many under a given limit end in 89?
	problem 92
	'''
	sieve = {d:0 for d in range(1,maximum + 1)}
	sieve[89],sieve[1] = 89,1
	j = 145
	chain = [j]
	while j != 89:
		chain.append(j)
		j = sum(int(k)**2 for k in str(j))
	sieve.update({c:89 for c in chain})
		
	for i,v in sieve.items():
		if v: continue
		chain = [i]
		while not sieve[i]:
			i = sum(int(j)**2 for j in str(i))
			chain.append(i)
		sieve.update({c:sieve[i] for c in chain})
	return sieve


