import collections
from problem_10 import get_all_primes_under
from problem_7 import is_prime

def concatenating_primes():
	'''
	problem 60
	'''
	primes = [str(p) for p in get_all_primes_under(10000)]
	parts = collections.defaultdict(set)
	
	def mirror_str_test(a,b):
			ab = a+b
			if len(ab) > 5:
				if is_prime(int(ab)) and is_prime(int(b+a)):
					return True
			elif ab in primes and b+a in primes: 
				return True 
			return False

	def concatenate_recurse(primes,found={}):
		if len(found) == 5: return found
		for i,a in enumerate(primes):
			if all(mirror_str_test(z,a) for z in found):
				result = concatenate_recurse(primes,found&a)
				if result: return result
		return False


	for i,a in enumerate(primes):
		found = {a}
		for j,b in enumerate(primes[i+1:]):
			if all(mirror_str_test(z,b) for z in found):
				found = {a,b}
				for k,c in enumerate(primes[j+1:]):
					if all(mirror_str_test(z,c) for z in found):
						found = {a,b,c}
						for l,d in enumerate(primes[k+1:]):
							if all(mirror_str_test(z,d) for z in found):
								found = {a,b,c,d}
								for e in primes[l+1:]:
									if all(mirror_str_test(z,e) for z in found):
										return {a,b,c,d,e}
	return 'FUCK'

def concatenating_primes():
	'''
	Problem 60, recursive solution
	'''

	primes = [str(i) for i in get_all_primes_under(10000)]

	@memo
	def mirror_str_test(a,b):
		ab = a+b
		if len(ab) > 5:
			if is_prime(int(ab)) and is_prime(int(b+a)):
				return True
		elif ab in primes and b+a in primes: 
			return True 
		return False

	def concatenate_recurse(primes,found=set()):
		if len(found) == 5: return found
		for i,a in enumerate(primes):
			if all(mirror_str_test(z,a) for z in found):
				result = concatenate_recurse(primes[i+1:],found|{a})
				if result: return result
		return False

	return concatenate_recurse(primes)

def memo(func):
	cache = {}
	def inner(*args):
		try:
			return cache[args]
		except KeyError:
			cache[args] = func(*args)
			return cache[args]
	return inner


