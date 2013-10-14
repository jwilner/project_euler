from problem_7 import is_prime

def is_circular_prime(n):
	'''
	return whether circle prime or not
	problem 35
	'''

	if type(n) != int:
		raise TypeError


	if not is_prime(n):
		return False

	s = str(n)
	length = len(s)
	i = 0
	while i < length:
		i += 1
		if not is_prime(int(rotate_string(s,i))):
			return False

	return True

def get_circular_primes_under(maximum):
	'''
	find all circular primes under a given maximum
	problem 35
	'''

	if type(maximum) != int:
		raise TypeError

	sieve = {d:0 for d in range(1,maximum+1)}

	for (i,v) in sieve.items():
		if v != 0:
			continue
		strung = str(i)
		length = len(strung)
		if '0' in strung:
			possibilities = [i] + [int(rotate_string(strung,j)) for j in range(1,length) if rotate_string(strung,j)[0] != '0']
		else:
			possibilities = [i]+[int(rotate_string(strung,j)) for j in range(1,length)]
		found = 1 if len([p for p in possibilities if is_prime(p)]) == length else -1
		sieve.update({p:found for p in possibilities})
	return [k for (k,v) in sieve.items() if v == 1]

def rotate_string(string,n):
	'''
	rotates characters around the given string
	problem 35
	'''
	return string[n:] + string[:n]


