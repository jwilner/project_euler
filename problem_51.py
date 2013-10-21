from collections import Counter
import itertools
from problem_10 import get_all_primes_under

def prime_digit_replacements(target = 7):
	'''
	find the lowest prime having a repeated digit that can be 
	replaced by other digits and thereby create other primes in the 'family' 
	problem 51
	'''
	wildcard = 'a'
	primes = get_all_primes_under(10**7)[5700:] #between 10**8 and 10**7
	primes = [(p,c) for (p,c) in [(p,Counter(p)) for p in [str(p) for p in primes]] if len(p) >= len(c) + 2]
	stripped = []
	for p,c in primes:
		for char in [e for e,v in c.items() if v == 3]:
			stripped.append((p.replace(char,wildcard),p))
		for char in [e for e,v in c.items() if v > 3]:
				for (a,b,c) in itertools.combinations([ind for ind,r_char in enumerate(p) if char == r_char],3):
					q = list(p)
					q[a],q[b],q[c] = wildcard,wildcard,wildcard
					stripped.append((''.join(q),p))
	stripped.sort()
	return stripped


