from problem_10 import get_all_primes_under
import math

def golbach_conjecture():
	'''
	prove that not all odd composite numbers can be formed from a prime and twice a square
	problem 46
	'''
	all_primes = get_all_primes_under(1000000)
	
	for i,p in enumerate(all_primes):
		test_point = p + 2
		while test_point < all_primes[i+1]: ##test_point must be a composite
			for poss_p in reversed(all_primes[:i+1]):
				rooted = math.sqrt((test_point - poss_p) / 2)
				if rooted == int(rooted):
					break
			else: return (p,test_point,all_primes[:i+1])
			test_point += 2


