from problem_10 import get_all_primes_under
from problem_7 import is_prime
import itertools

def get_quadratic(n,a,b):
	'''
	returns a basic quadratic equation's value
	problem 27
	'''
	return n**2+n*a+b

def quadratic_prime_with_a_and_b_under(maximum):
	'''
	returns a list of tuple (a,b) from 'n^2 + an + b' and an integer
	representing how effective that quad is at predicting primes for
	consecutive n values.

	b must be a prime (0 + 0a + b) if at all effective, and a+b+1 must
	be a prime to get 2

	problem 27
	'''
	primes_under_max = get_all_primes_under(maximum)
	products = itertools.product(range(-maximum,maximum+1),primes_under_max)
	terms = {(a,b):2 for (a,b) in products if a+b+1 in primes_under_max or is_prime(a+b+1)}
	for (a,b),num in terms.items():
		n = 2
		q = get_quadratic(n,a,b)
		while q in primes_under_max if q < maximum else is_prime(q):
			n += 1
			q = get_quadratic(n,a,b)

		terms[(a,b)] = n-1
	return terms


