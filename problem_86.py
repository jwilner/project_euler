

def prime_power_triples(limit=50000000):
	'''
	naive approach
	problem 86
	'''

	max_sq_root,max_cube_root,max_quap_root = int((limit - 2**3-2**4)**.5),int((limit - 2**2-2**4)**(1/3.0)),int((limit - 2**2-2**3)**.25)
	primes = get_all_primes_under(max_sq_root)
	cube_index,quap_index = primes.index(min(primes,key=lambda x:abs(x-max_cube_root))),primes.index(min(primes,key=lambda x:abs(x-max_cube_root)))
	cube_roots,quap_roots = primes[:cube_index+1],primes[:quap_index+1]

	triples = set()

	for sq in primes:
		for cube in cube_roots:
			for quap in quap_roots:
				summation = sq**2+cube**3+quap**4
				if summation > limit: break
				triples.add(summation)

	return triples


