import math, itertools, functools, collections, random, operator, fractions

def is_palindrome(n):
	'''
	returns true or false depending on whether input string is palindromic
	problems 36, 55
	'''
	if type(n) != str:
		raise TypeError
	return True if n == n[::-1] else False

def lattice_path(n):
	'''
	grid representing problem space
	problem15
	'''
	if type(n) != int:
		raise TypeError

	grid = []
	for i in range(1,n+2):
		grid.append([0]*(n+2))
	x = 0;

	while x < n+1:
		y = 0
		while y < n+1:
			ways = 0
			if x > 0:
				ways = ways + grid[x-1][y]
			if y > 0:
				ways = ways + grid[x][y-1]
			if ways == 0:
				ways = 1
				grid[x][y] = ways
			y = y + 1
		x = x + 1

	return grid

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

def maximum_path(triangle):
	'''
	find the maximum path through an integer triangle such as in
	problem 18, problem 67

	input triangle is a 2-D list where internal list represents a
	rung and each list item integer within an upfacing triangle

	proceeds from bottom row, adding value of larger of two adjacent
	items on bottom to item on top; once it reaches the apex,
	the sum there is the sum of the greatest possible path. 	
	'''

	delta = reversed(triangle)

	for i,row in enumerate(delta):
		if i == 0:
			continue
		for j,val in enumerate(row):
			oldI = i - 1
			delta[i][j] = val + max(delta[oldI][j:j+2])		

	return delta[i][j]

def return_word_value(name):
	'''
	takes a string and returns its 1-to-26 string value
	problem22
	'''
	if(type(name) != str):
		raise TypeError

	value = 0
	for character in name.lower():
		value = value + ord(character)-96
	return value

class triangleNumbers:
	'''
	for dealing with triangle numbers
	problem 12
	'''
	def __init__(self):
		self.cache = {1 : 1}

	def get_nth_triangle_number(self,n):
		'''finds the nth triangle number'''
		if n in self.cache:
			return self.cache[n]
		new_val = (n*(n+1))/2
		self.cache[n] = new_val
		return new_val
	def get_first_triangle_number_with_n_factors(self,n):
		'''
		returns the position of the first triangle number
		 with at least n factors'''
		i = 1
		num_factors = 1
		while num_factors < n:
			i = i + 1
			factors = factorNumber(self.getNthTriangleNumber(i))
			num_factors = len(factors)
		return (i,num_factors)

def factorNumber(n):
	'''
	returns all factors of a number, including 1 and itself
	problem 22
	'''
	factors = []

	limit = math.floor(math.sqrt(n))
	i = 1
	while i <= limit:
		if n % i == 0:
			factors.extend([i,n//i])
		i = i+1
	return factors


def getCollatz(n):
	'''
	Return the next term in a collatz sequence
	problem 14
	'''
	return n / 2 if n % 2 == 0 else (n*3)+1

def getCollatzSequence(n):
	'''
	Returns a list representing a collatz sequence beginning with the given number.
	problem 14
	'''
	a_list = [n]
	while n != 1:
		n = getCollatz(n)
		a_list.append(n)

	return a_list

def getLongestCollatzSequenceUnder(max):
	'''
	returns a list representing the longest collatz sequence under the provided maximum
	problem 14
	'''
	longest = 1
	length = 1
	i = 1
	while i <= max:
		possLength = len(getCollatzSequence(i))
		if possLength > length:
			longest = i
			length = possLength
		i = i + 1
	return {longest : length}

def getFirstFibOfLength(digits):
	'''
	get first fibonacci number of given length
	problem25
	'''
	if type(digits) != int:
		raise TypeError

	a,b = 0, 1
	length = 1
	i = 0
	while len(str(a)) < digits:
		i = i + 1
		a , b = b, a+b
	return i

def is_prime(n):
	'''
	test whether a number is prime or not
	problem 7, among others
	from notes on problem 7
	'''
	if type(n) != int:
		raise TypeError
	if n <= 1:
		return False
	if n < 4: ## {2,3}
		return True
	if n % 2 == 0:
		return False
	if n < 9: ## {5,7}
		return True
	if n % 3 == 0:
		return False
	else:
		r = math.floor(math.sqrt(n)) ##r*r = n
		f = 5
		while f <= r:
			if n % f == 0:
				return False
			if n % (f + 2) == 0:
				return False
			f += 6
	return True

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

def get_all_primes_under(maximum):
	'''
	returns list of all primes under maximum ('sieve of eratosthones')
	problem 10, problem 27
	'''
	boundary = math.floor((maximum - 1) / 2) ##only odds need be considered
	sieve = {d:False for d in range(1,boundary+1)}	
	'''
	sieve index i corresponds to odd number 2i + 1
	'''

	cross_limit = (math.floor(math.sqrt(maximum)) -1) / 2
	'''
	only need to look for primes as far as square root of maximum
	'''
	i = 1
	while i <= cross_limit:
		if not sieve[i]: ##then 2i + 1 prime
			for j in range(2*i*(i+1),boundary+1,(2*i)+1):
				sieve[j] = True
		i += 1
		'''
		If i is false, then 2i+i is prime, and all multiples of 2i+i
		less than (2i+1)^2 will have already been marked non-prime 
		(as multiples of numbers less than 2i + 1); index of (2i+1)^2
		is 2i*(i+1); start at that index, and 
		'''
	return [2]+[2*i+1 for (i,v) in sieve.items() if v == False]

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

def champernowne_constant_position(n):
	'''
	returns nth fractional position of champernowne constant
	problem 40
	'''
	# total - positions - here - per - num value
	# 9     	1-9   		9      1     1-9
	# 189   	10-189   	180    2     10-99
	# 2889     	190-2889	2700   3     100-999
	# 38889		2890-38889	36000  4  	 1000-9999

	#if someone asks for the nth position, find p
	p, range_start = 1,1
	while n - range_start >= 9*p*(10**(p-1)):
		range_start += 9*p*(10**(p-1))
		p += 1

	rel_position = n - range_start
	num_integer = rel_position // p
	num_digit = rel_position % p

	our_integer = 10**(p-1) + num_integer
	strung = str(our_integer)
	return int(strung[num_digit])


# def find_recurring_cycle(s):
# 	'''
# 	find the greatest recurring cycle in a given string
# 	problem 26
# 	'''
# 	#1234512345
# 	if type(s) != str:
# 		raise TypeError 

# 	tree = []
# 	i = 1
# 	found = false
# 	while not found:
# 		tree[] = s[:i]

def solve_quadratic(a,b,c):
	'''
	uses determinant and quadratic formula to return roots given
	coefficients
	'''
	d = (b**2)-(4*a*c)
	if d < 0:
		return tuple()
	if d == 0:
		return tuple([(-b)/(2*a)])
	else:
		rooted = d**.5
		return ((-b+rooted)/(2*a),(-b-rooted)/(2*a))

def is_triangle_number(n):
	'''
	tests whether number is a triangle number using quadratic formula
	problem 45
	'''
	roots = solve_quadratic(1,1,-2*n)
	return True if [r for r in roots if r > 0 and r == int(r)] else False

def is_pentagonal_number(n):
	'''
	tests whether number is a pentagonal number using quadratic formula
	problem 45
	'''
	roots = solve_quadratic(3,-1,-2*n)
	return True if [r for r in roots if r > 0 and r == int(r)] else False

def is_hexagonal_number(n):
	'''
	tests whether number is a hexagonal number using quadratic formula
	problem 45
	'''
	roots = solve_quadratic(2,-1,-n)
	return True if [r for r in roots if r > 0 and r == int(r)] else False

def get_nth_hexagonal_number(n):
	'''
	returns the nth item from the hexagonal number sequence (subset of triangle numbers)
	problem 45
	'''
	return 2*(n**2)-n

def find_steps_to_palindrome(maximum,limit = 50):
	'''
	Find the number of iterations it takes to make a number into a palindrome through 
	reverse-and-add process for numbers <= maximum; numbers that don't become a 
	palindrome within 'limit' iterations (lychrel numbers) are designated with -1
	problem 55
	'''
	sieve = {a:0 for a in range(maximum+1)}
	for i,v in sieve.items():
		if v > 0: #then number of steps to palindrome has been found
			continue
		steps = [i]
		n = i #need to access i later, so preserve
		while len(steps) < limit:
			n += int(''.join(s for s in reversed(str(n))))
			if is_palindrome(str(n)): #check if palindrome before adding; otherwise palindrome would be included in steps
				steps.reverse() #reverse list so that indices express no. of 0-based steps from palindrome 
				sieve.update({val:ind+1 for ind,val in enumerate(steps) if val <= maximum}) 
				break
			steps.append(n)
		else: #if length of steps surpasses limit, this fires
			sieve[i] = -1 ##connotes lychrel
	return sieve

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

def is_permuted_multiple(n,iters = 6):
	'''
	return true or false if the digits of n and the digits of its multiples up to n x iters are identical
	problem 52
	'''
	n_set = set(str(n))
	for i in range(2,iters+1):
		if set(str(i*n)) != n_set:
			return False
	return True

def find_lowest_possible_integer(i,test):
	'''
	apply test to every integer equal to and greater than i, and return the first integer for which the test evaluates true 
	'''
	if not hasattr(test, '__call__'):
		raise TypeError

	while not test(i):
		i += 1

	return i

def combinations_over(n_min = 22,n_max = 101,maximum = 1000000):
	'''
	find every nCr number of combinations greater than n for the given possible range of n
	problem 53
	'''
	combinations = {}
	for n in range(n_min+1,n_max):
		found = {}
		r = math.ceil(n/2)
		while r > 0:
			ncr = (math.factorial(n)) / (math.factorial(r)*(math.factorial(n-r)))
			if ncr <= maximum:
				break
			found[(n,r)] = ncr
			r -= 1
		found.update({(n,n-r):ncr for ((n,r),ncr) in found.items() if n-r != r})
		combinations.update(found)
	return combinations

def count_coins(coins = [1,2,5,10,20,50,100,200],value=200):
	table = [0 for x in range(value + 1)]
	m = len(coins)
	table[0] = 1
	for i in range(0,m):
		for j in range(coins[i],value+1):
			table[j] += table[j-coins[i]]
	return table[value]

def factors(n):    
	return set(functools.reduce([1].__add__,([i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)))

def truncatable_primes(maximum = 1000000):
	'''
	find all eleven 'truncatable' primes
	problem 37
	'''
	poss_digits = set('1379')
	all_primes = get_all_primes_under(maximum)
	poss_primes = [p for p in [str(p) for p in all_primes] if set(p[1:]) <= poss_digits]
	#primes can only be composed of the digits 1,3,7, and 9
	#after the first digit
	
	final_primes = []
	for p in poss_primes:
		found = True
		length = len(p)
		for i in range(0,length):
			if not is_prime(int(p[i:])) or not is_prime(int(p[:i+1])):
				found = False
				break
		if found: final_primes.append(int(p))
	return final_primes

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

def pandigital_prime(num_digits = 4):
	'''
	find largest number that uses all digits 1 through num_digits and is prime 
	problem 41
	'''
	for num_d in r6ange(num_digits,0,-1):
		digits = [str(d) for d in range(1,num_d+1)]
		perms = itertools.permutations(''.join(reversed(digits)))
		for i in perms:
			num = int(''.join(i))
			if is_prime(num): return num

def pandigital_products():
	'''
	find all products whose producing equation has every digit 1 to 9 inclusive once; e.g. 39 x 186 = 7254
	problem 32
	'''
	possibilities = itertools.permutations(str(i) for i in range(1,10))
	identities  = [(int(''.join(x[5:])),x[:5]) for x in possibilities]
	return {p for p,x in identities if int(''.join(x[:2]))*int(''.join(x[2:]))==p or int(''.join(x[:1]))*int(''.join(x[1:])) == p}


def prime_permutations():
	'''
	finds all primes (necessarily 4 digit primes) that are in an arithmetic sequence and in which each is a permutation of the other
	problem 49
	'''
	all_primes = get_all_primes_under(10000)
	four_digit_primes = all_primes[all_primes.index(min(all_primes, key=lambda x:abs(x-1000))):]
	groups = []
	possibilities = dict(zip(four_digit_primes,[False] * len(four_digit_primes)))
	for p,v in possibilities.items():
		if v == True:
			continue
		perms = {int(''.join(i)) for i in itertools.permutations(str(p))}
		overlap = []
		for k in perms:
			if k in possibilities.keys():
				possibilities[k] = True
				overlap.append(k)
		if len(overlap) >= 3:
			groups.append(tuple(sorted(overlap)))

	prime_permutations = set()
	for g in groups:
		for j in itertools.permutations(g,3):
			j = sorted(j)
			if is_arithmetic_sequence(j[0],j[1],j[2]):
				prime_permutations.add(tuple(j))
	return prime_permutations

def is_arithmetic_sequence(a,b,c):
	return True if (a + c)/2 == b else False

	# possibilities = [int(''.join(a)) for a,b in collections.Counter([tuple(sorted(str(p))) for p in four_digit_primes]).items() if b > 2]
	# permuted =  [p for p in four_digit_primes if p in possibilities] #this is a list of four digit prime numbers having at least two permutations of themselves also present in the list

def digital_sums_of_square_roots(limit = 100):
	'''
	for natural numbers one to limit, find the digital sums of all irrational square roots
	problem 80
	'''
	import decimal
	irrationals = []	
	for n in range(1,limit+1):
		rooted = decimal.Decimal(n).sqrt()
		if int(rooted) != rooted:
			irrationals.append(str(int(rooted*10**99)))
	return [sum([int(d) for d in i]) for i in irrationals]

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

def convergent_of_e(n):
	'''
	returns the nth convergent of the continued fraction of e
	problem 65
	'''
	from fractions import Fraction
	n -= 1
	convergent_points = []#collections.deque()
	for i in range(1,n+1):
		if (i - 2) % 3 == 0:
			convergent_points.append(int(2*(i+1)/3))
		else:
			convergent_points.append(1)
	conv = 0
	while convergent_points:
		conv = Fraction(1/(convergent_points.pop() + conv))
	return Fraction(2+conv)

def proper_reduced_fractions_in_range(minimum = '1/3',maximum = '1/2',denominator = 8):
	'''
	returns all proper reduced fractions with a limited denominator between two given values
	problem 73
	'''
	
	minimum,maximum = Fraction(minimum),Fraction(maximum)

	all_fractions = set()
	for d in range(denominator,math.floor(denominator/2),-1):
		max_n,min_n = math.ceil(d * maximum), math.ceil(d * minimum)
		for n in range(min_n,max_n):
			all_fractions.add(Fraction(n,d))

	all_fractions -= {minimum,maximum}	
	return all_fractions

def pandigital_multiples(digits = 9):
	'''
	find the largest pandigital 1 to digits number that can be formed by concatenating the products of n and each of {1,2 ... i}
	problem 38
	'''
	max_length = 4
	biggest = 0
	previous_biggest = []
	final_chars = set(str(i) for i in range(1,digits+1))
	for i in range(1,10**max_length):
		chars = set()
		strung_num = ''
		nums = []
		m = 0
		while len(strung_num) < digits:
			m += 1
			num = i * m
			# if len(previous_biggest) >= m and num < previous_biggest[m-1]:
			# 	bypass = True
			# 	break
			nums.append(num)
			strung = str(num)
			chars |= set(strung)
			strung_num += strung
			if len(chars) < len(strung_num):
				break
		else:
			number = int(strung_num)
			if chars == final_chars and number > biggest :
				previous_biggest, biggest = nums,number
		if i > 300 and i < 400:
			print(nums)
	return previous_biggest

def n_convergents_of_root_two(i):
	'''
	returns the nth convergent of the continued fraction of root two
	problem 65
	'''
	n,d = 1,1
	fracs = []
	for j in range(0,i):
		n,d = n+d+d,n+d
		fracs.append(Fraction(n,d))
	return fracs

def nth(iterable, n, default=None):
    '''
    Returns the nth item or a default value
    '''
    return next(itertools.islice(iterable, n, None), default)

def brent_algorithm(seq_gen_func):
	'''
	brent algorithm finds recurring pattern and returns the 
	'''
	dec_gen = seq_gen_func()
	position = steps_taken = step_limit = 1
	found = False
	tortoise = None
	hare = next(dec_gen)
	while tortoise != hare:
		if steps_taken == step_limit:
			tortoise = hare
			step_limit *= 2
			steps_taken = 0
		steps_taken += 1
		position += 1
		hare = next(dec_gen)

	#at this point, period must equal steps_taken, but we still need entry point
	#give tortoise and hare their own generators
	dec_gen_2,dec_gen_3 = seq_gen_func(), seq_gen_func()
	period = steps_taken
	tortoise = next(dec_gen_2)
	hare = next(itertools.islice(dec_gen_3,period,None))
	mu = 0
	while tortoise != hare:
		mu += 1
		tortoise, hare = next(dec_gen_2), next(dec_gen_3)
	return (mu,period)

def find_decimal_cycles(max = 1000):
	'''
	find all decimal cycles under a given limit
	problem 26
	'''
	nums = [i for i in range(1,max+1)]
	for i in range(1,len(nums)):
		d = i
		def gen_func():
			a = 1 % d
			while True:
				yield a
				a = (10 * a) % d
		nums[d] = brent_algorithm(gen_func)
	return nums

def substring_divisibility():
	'''
	first define rules and then use them to limit eachother; ultimately means only two possiblities for last five characters
	d5d6d7d8d9d10 must be either 357289 or 952867, leaving only permutations of, respectively, 0146,0134 for the d1d2d3d4
	problem 43
	'''

	nums = []
	d = {'0146':'357289','0134':'952867'}
	for first_four,last_five in d.items():
		for i in itertools.permutations(first_four):
			s = ''.join(i)+last_five
			if int(s[1:4]) % 2 == 0 and int(s[2:5]) % 3 == 0:
				nums.append(int(s))
	return nums

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


def pollard_brent(n):
	'''
	implementation of pollard brent algorithm for finding a prime factor of n
	https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/
	'''
	if n % 2 == 0: return 2
	if n % 3 == 0: return 3
	y, c, m = random.randint(1, n-1), random.randint(1, n-1), random.randint(1, n-1)
	g, r, q = 1, 1, 1
	while g == 1:
		x = y
		for i in range(r):
			y = (pow(y, 2, n) + c) % n
		k = 0
		while k < r and g==1:
			ys = y
			for i in range(min(m, r-k)):
				y = (pow(y, 2, n) + c) % n
				q = q * abs(x-y) % n
			g = fractions.gcd(q, n)
			k += m
		r *= 2
	if g == n:
		while True:
			ys = (pow(ys, 2, n) + c) % n
			g = fractions.gcd(abs(x - ys), n)
			if g > 1:
				break
	return g


small_primes = get_all_primes_under(1000)
def prime_factors(n):
	'''
	prime factorization employing pollarrd brent algorithm
	http://stackoverflow.com/questions/4643647/fast-prime-factorization-module
	'''
	factors = []

	limit = int(n ** .5) + 1
	for checker in small_primes:
		if checker > limit: break
		while n % checker == 0:
			factors.append(checker)
			n //= checker
			limit = int(n ** .5) + 1
		if checker > limit: break

	if n < 2: return factors

	while n > 1:
		if is_prime(n):
			factors.append(n)
			break
		factor = pollard_brent(n) # trial division did not fully factor, switch to pollard-brent
		factors.extend(prime_factors(factor)) # recurse to factor the not necessarily prime factor returned by pollard-brent
		n //= factor
	return factors

def numbers_with_n_distinct_factors(num_distinct = 4):
	'''
	Find the first four integers each with four distinct prime factors 
	problem 47
	'''
	Counter = collections.Counter
	number_factors = [[],[]]
	for i in range(2,1000000):
		first = [i**v for i,v in Counter(prime_factors(i)).items()]
		number_factors.append(first)
		if len(first) >= num_distinct:
			test_set = set(first)
			b = number_factors[-num_distinct:-1]
			expected = num_distinct * 2
			for c in b[::-1]:
				test_set.update(c)
				if len(test_set) < expected:
					break
				expected += num_distinct
			else:
				return number_factors[-num_distinct:]

def steps_with_euclids_algorithm(x,y):
	i = 0
	while y != 0:
		i += 1
		x, y = y, x % y
	return i

def classic_sum(n):
	dictionary = {(x,y):0 for x in range(1,n+1) for y in range(1,x+1)}
	for (x,y) in list(dictionary.keys()):
		if dictionary[(x,y)]:
			continue
		steps = steps_with_euclids_algorithm(x,y)
		if x != y:
			dictionary[(x,y)],dictionary[(y,x)] = steps,steps + 1
		else:
			dictionary[(x,y)] = steps
	return dictionary

def sum_of_steps_2(n):
	import fractions
	d = collections.defaultdict(int)
	for x in range(1,1001):
		for y in range(1,1000):
			a,b = x,y
			while b != 0:
				d[(a,b)] += 1
				a,b = b, a%b
	lookup = {(e,f):steps_with_euclids_algorithm(e,f) for (e,f),g in sorted(d.items(),reverse=True,key=lambda x:x[1])}

	summation = n #that is, all multiples of E(1,1) = 1 
	summation += sum([n//c for c in range(2,n+1)])*3 # that is, steps all multiples of (i,1) where i between 2 and n inclusive
	summation += sum([n//c for c in range(3,n+1) if c % 2 != 0])*5 #that is, steps for all multiples of (i,2) where i between 3 and n inclusive
	summation += sum([(n//c)*(2*(c%3)+3) for c in range(4,n+1) if c % 3 != 0])#that is, steps for all multiples of (i,3) where i >= 4
	for x in range(5,n+1):
		prime = is_prime(x)
		for y in range(4,x):
			if not prime and fractions.gcd(x,y) != 1:
				continue
			steps = 0
			e,f = x,y
			while f != 0:
				if e < 1000 and (e,f) in lookup:
					steps += lookup[(e,f)]
					break
				steps += 1
				e, f = f, e % f			
			a,b = x,y
			while a <= n:
				summation += (steps*2)+1
				a,b = a+x,b+y
	return summation

def euc(x,y):
	steps = 0
	a,b = x,y
	while b != 0:
		steps += 1
		a,b = b, a % b
	return (a,steps)

# d = collections.defaultdict(int)
# for x in range(1,1001):
# 	for y in range(1,1000):
# 		a,b = x,y
# 		while b != 0:
# 			d[(a,b)] += 1
# 			a,b = b, a%b
# lookup = {(e,f):euc(e,f) for (e,f),g in sorted(d.items(),reverse=True,key=lambda x:x[1])}

def a_third_try(n):
	division_point = 2
	total = n # x = y diagonal
	for y in range(1,1+n//division_point):
		num_cycles = (n-y) // y
		left_over = (n-y) % y
		len_cycle = y
		pattern = []
		for x in range(y+1,2*y+1): #start just right of diagonal
			if y != 1 and x % y == 0:
				pattern.append(0)
				continue
			steps = 0
			a,b = x,y
			while b:
				steps += 1
				a,b = b, a % b
			if a == 1:
				pattern.append(steps)
			else:
				pattern.append(0)
		full_pattern = pattern*num_cycles+pattern[:left_over]
		row = 0
		for i,v in enumerate(full_pattern):
			if not v:
				continue
			x = i + y + 1
			implieds = (n // x)
			row += (implieds)*v 
		total += (row)*2 + n - y
	for y in range(1+n//division_point,n):
		sequence = []
		for x in range(y+1,n+1): #start just right of diagonal, which has already been accounted for
			if y != 1 and x % y == 0:
				pattern.append(0)
				continue
			steps = 0
			a,b = x,y
			while b:
				steps += 1
				a,b = b, a % b
			if a == 1:
				sequence.append(steps)
			else:
				sequence.append(0)
		row = 0
		for i,v in enumerate(sequence):
			if not v:
				continue
			x = i + y + 1
			implieds = (n // x)
			row += (implieds)*v 
		total += (row)*2 + n - y
	return total

def compare_approaches(n):
	a = sum_of_steps(n)
	b = classic_sum(n)
	difference = {}
	for i in a:
		if a[i] != b[i]:
			difference.update({i:{'a':a[i],'b':b[i]}})
	return difference

class Totient:
    def __init__(self, n):
        self.totients = [1 for i in range(n)]
        for i in range(2, n):
            if self.totients[i] == 1: #then prime b/c not yet hit by later steps a la sieve
                for j in range(i, n, i): #every multiple of i less than n
                    self.totients[j] *= i - 1 #increase each multiple's number of totients by factor (i-1), b/c every prime p has phi(p) == p-1
                    k = j / i # k is another integer (b/c corresponds to iteration) factor of j
                    while k % i == 0: #if k has powers of i in it
                        self.totients[j] *= i
                        k /= i
    def __call__(self, i):
        return self.totients[i]

def consecutive_prime_sum(lim = 1000):
	'''
	find the longest sequence of primes summing to a prime beneath lim
	problem 50
	'''
	all_primes = get_all_primes_under(lim)
	longest = {'length':2,'sum':5}
	min_sum = 5
	while longest['length'] < len(all_primes):
		p = all_primes.pop()
		if p < min_sum:
			print('hit min sum ',min_sum)
			break
		med = int(p/2)
		b = min(range(len(all_primes)), key=lambda i: abs(all_primes[i]-med))
		a = b-1
		value = sum(all_primes[a:b+1])
		primes_underneath = sum(all_primes[:a])
		while a > 0:
			if value > p:
				value -= all_primes[b]
				b -= 1
				a -= 1
				value += all_primes[a]
				primes_underneath -= all_primes[a]
			elif value < p:
				if primes_underneath < p-value:
					break
				a -= 1
				value += all_primes[a]
				primes_underneath -= all_primes[a]
			else:
				length = b-a+1
				if length > longest['length']:
					longest['length'],longest['sum'] = length,value
					min_sum = sum(all_primes[:longest['length']])
				value -= all_primes[b]
				b -= 1
	return longest

def alternate_prime_sum():
	ps=get_all_primes_under(3946)
	mt,ms,mcps=len(ps),sum(ps),(0,0)
	while mt>mcps[0]:
	  ls=ms if ms%2 else ms-1
	  while not is_prime(ls): ls-=2
	  k,ts=0,ms
	  while ts-ls>0: ts-=ps[k]; k+=1
	  if ts==ls and mt-k>mcps[0]: mcps=(mt-k,ts)
	  mt-=1
	  ms-=ps[mt]
	    
	print(mcps)

def eul50():
    primes = get_all_primes_under(10**6)
    d = {}
    running = 0
    for p in primes:
        if p > 50000: break
        running += p
        d[p] = running
    b = sorted(d.keys())
    best = (21, 953)
    e = {}
    for i in range(len(b)):
        for j in range(i + (best[0] if best[0]%2 == 1 else best[0]-1), len(b)-1, 2):
            val = d[b[j]] - d[b[i]]
            if val > 1000000: break
            if val in primes and j-i > best[0]: best=(j-i, val)
    return best

def prime_digit_replacements(target = 7):
	'''
	find the lowest prime having a repeated digit that can be 
	replaced by other digits and thereby create other primes in the 'family' 
	problem 51
	'''
	wildcard = 'a'
	from collections import Counter
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

def spiral_prime_ratio(i = 10):
	'''
	find the first ring of spiral prime at which the ratio of primes 
	is less than given %
	problem 58
	'''

	percent = 100/i
	primes = 0
	corners = 1
	for i in range(2,10**6,2):
		side = i+1
		square = side**2
		primes += len([c for c in range(1,4) if is_prime(square-(c*i))])
		corners += 4
		if percent*primes < corners:
			return (side,primes,corners)

keylog = ['319', '680', '180', '690', '129', '620', '762', '689', '762', '318', '368', '710', '720', '710', '629', '168', '160', '689', '716', '731', '736', '729', '316', '729', '729', '710', '769', '290', '719', '680', '318', '389', '162', '289', '162', '718', '729', '319', '790', '680', '890', '362', '319', '760', '316', '729', '380', '319', '728', '716']

def keylog_analysis(keylog):
	'''
	find the shortest possible passcode
	problem 79
	'''
	from collections import defaultdict
	rules = set()
	for code in keylog:
		rules.update([tuple(code[:2]),tuple(code[1:])])

	rules = list(rules)
	beginning = ''
	end = ''
	while rules:
		first = set()
		last = set()
		record = defaultdict(list)
		for rule in rules:
			first.add(rule[0])
			last.add(rule[1])
			record[rule[0]].append(rule)
			record[rule[1]].append(rule)
		first_term = first.difference(last)
		last_term = last.difference(first)
		if len(first_term) == 1:
			ft = first_term.pop()
			beginning += ft
			for f in record[ft]:
				if f in rules: rules.remove(f)
		if len(last_term) == 1:
			lt = last_term.pop()
			end = lt+end
			for l in record[lt]:
				if l in rules: rules.remove(l)
	return beginning+end

class Roman:
	'''
	A class for dealing with Roman numerals
	Problem 89
	'''
	_numerals = [('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1)]
	_cache = {}

	def __init__(self):
		self._by_length = sorted(self._numerals,reverse = True,key=lambda x:len(x[0]))
		self._by_value = sorted(self._numerals,reverse = True,key=lambda x:x[1])

	def roman_to_arab(self,r_num):
		if type(r_num) != str:
			raise TypeError
		if r_num in self._cache:
			return self._cache[r_num]
		tally = 0
		original = r_num
		for (roman,arab) in self._by_length:
			if roman in r_num:
				times, r_num = r_num.count(roman), r_num.replace(roman,'')
				tally += arab*times
		self._cache[original] = tally
		return tally

	def arab_to_roman(self,a_num):
		if type(a_num) != int:
			raise TypeError
		if a_num in self._cache:
			return self._cache[a_num]
		original = a_num
		r_num = ''
		for (roman,arab) in self._by_value:
			if a_num >= arab:
				r_num += roman*(a_num//arab)
				a_num %= arab
		self._cache[original] = r_num
		return r_num

def partition(n):
	'''
	find the lowest integer for which the number
	of its partitions is a multiple of 1,000,000
	problem 78
	'''
	from itertools import takewhile,cycle,count
	partitions = {}
	generalized_pentagonals = sorted([i for i in pentagon_gen(-250,250)])[1:]
	def part(n):
		if n <= 1: return 1
		if n not in partitions:
			signs = cycle([1,1,-1,-1])
			pentagonals = takewhile(lambda p:p <= n, generalized_pentagonals)
			partitions[n] = sum(sign*part(n-p) for sign,p in zip(signs,pentagonals))
		return partitions[n]
	return part(n)

def cube_permutations(n=5,start=3000):
	'''
	find the lowest cube the digits of which can be permuted to produce five other cubes
	problem 62
	'''
	from collections import defaultdict
	cubes = defaultdict(list)
	while True:
		cube = start**3
		sig = ''.join(sorted(str(cube)))
		cubes[sig].append(cube)
		if len(cubes[sig]) >= n:
			return cubes[sig][0]
		start += 1

def proper_reduced_fraction_to_left(target='3/7',d_max=8):
	'''
	find the reduced proper fraction directly
	to the left of the given target
	problem 71
	'''

	from fractions import Fraction
	import bisect

	target = Fraction(target)
	frac_list = [target]
	targ_index = 0

	multiplier = (d_max-target.denominator)//target.denominator
	n,d = target.numerator*multiplier,target.denominator*multiplier
	if not multiplier:
		n,d = 0,1

	while d < d_max:
		while n/d < target:
			n += 1
		n -= 1
		f = Fraction(n,d)
		i = bisect.bisect(frac_list,f)
		if i == targ_index:
			frac_list.insert(i,f)
			n,d,targ_index = n+1,d+1,targ_index+1
			continue
		n,d = n+1,d+1
	return frac_list[targ_index-1]

def fraction_cheating(n=3,d=7,limit = 1000000):
	'''
	find the reduced proper fraction directly
	to the left of the given target
	problem 71
	'''
	from fractions import Fraction
	real = Fraction(n,d)
	approx = Fraction(n/d)
	while approx.limit_denominator(limit) == real: #Fraction(7720456504063707, 18014398509481984)
		approx = Fraction(approx.numerator-1,approx.denominator)
	return approx #Fraction(3595117, 8388608)???

def digit_factorials(limit = 1000):
	'''
	Digit factorial chains tend to repeat. Return the length of repeating chains under a given limit
	problem 74
	'''	
	#in loop 654321321, 6,5,4 would have 6,5,4 'non-repeating' numbers, but 3,2,1 would each have 3, because they occur w/in loop
	from math import factorial

	factorials = {str(i):factorial(i) for i in range(0,10)}
	def factorialize_digits(n): 
		return sum(factorials[d] for d in str(n))

	chain_lengths = {0:2,1:1,2:1,169:3,363601:3,1454:3,871:2,45361:2,45362:2,872:2,69:5,363600:4,78:4,45360:3,540:2,145:1}
	for i in range(3,limit):
		if i in chain_lengths:
			continue
		chain = [i]
		f = factorialize_digits(i)

		while f not in chain:
			if f in chain_lengths: #then use cached info
				total_length = len(chain) + chain_lengths[f]
				update_dict = {v:total_length-i  for i,v in enumerate(chain)}
				break
			chain.append(f)
			f = factorialize_digits(f)
		else: #no cached info found, but loop detected (f in chain)
			chain_length = len(chain)
			loop_start = chain.index(f)
			loop_length = chain_length - loop_start
			update_dict = {v:chain_length-i if i < loop_start else loop_length for i,v in enumerate(chain)}
		chain_lengths.update(update_dict)
	return chain_lengths

def digit_factorial_chain(n):
	d = []
	while n not in d:
		d.append(n)
		yield n
		n = factorialize_digits(n)

def n_power_n_digits():
	'''
	how many numbers are there with n digits that can be expressed as some number to the n
	problem62
	'''
	success = set()
	for i in range(1,10):
		j = 1
		powed = i**j
		digs = len(str(i**j))
		while j <= digs+1:
			if j == digs:
				success.add(powed)
			j += 1
			powed = i**j
			digs = len(str(i**j))
	return success

def totient(n):
	return int(n * functools.reduce(operator.mul,[1-fractions.Fraction(1,i)  for i in set(prime_factors(n))]))

class poker_hand:
	order = ('2','3','4','5','6','7','8','9','T','J','Q','K','A')
	def __init__(self,cards):
		self._cards,self._originals = sorted((self.order.index(c[0]),c[1]) for c in cards), cards
		self.hand_values = (('high card',tuple()),('one_pair',(self.get_pairs,)),('two pairs',(self.is_two_pair,)),('three of a kind',(self.get_three_of_a_kind,)),('straight',(self.is_straight,)),('flush',(self.is_flush,)),('full house',(self.get_three_of_a_kind,self.get_pairs)),('four of a kind',(self.get_four_of_a_kind,)),('straight flush',(self.is_flush,self.is_straight)))
	def is_flush(self):
		try:
			return self._flush
		except AttributeError:
			suit = self._cards[0][1]
			self._flush = True
			for c in self._cards[1:]:
				if c[1] != suit:
					self._flush = False
					break
			return self._flush
	def is_straight(self):
		try:
			return self._straight
		except AttributeError:
			self._straight = True
			last_pos = self._cards[0][0]
			for c in self._cards[1:]:
				if c[0] != last_pos + 1:
					self._straight = False
					break
				last_pos = c[0]
			return self._straight
	def get_groups(self):
		try:
			return self._groups
		except AttributeError:
			from itertools import groupby
			from collections import defaultdict
			self._groups = defaultdict(set)
			return_pos = lambda x:x[0]
			self._cards.sort(key=return_pos)
			for k,g in groupby(self._cards,key=return_pos):
				grouped = tuple(g)
				size_group = len(grouped)
				self._groups[size_group].add(grouped)
			return self._groups
	def get_pairs(self):
		return self.get_groups()[2]
	def is_two_pair(self):
		return True if len(self.get_groups()[2]) == 2 else False
	def get_three_of_a_kind(self):
		return self.get_groups()[3]
	def get_four_of_a_kind(self):
		return self.get_groups()[4]
	def get_high_card(self):
		#if the cards are grouped, it goes through them from big group to small;
		#if ungrouped, each individual card is treated as a group of one, so this will still serve up proper values for comparing five card hands
		try:
			return next(self._high_groups)
		except AttributeError:
			from itertools import chain
			groups = sorted((i for i in chain(*self.get_groups().values())),key=lambda x:(len(x),x[0]),reverse=True)
			self._high_groups = (g[0][0] for g in groups)
			return next(self._high_groups)
	def get_hand_value(self):
		try:
			return self._value
		except AttributeError:
			best_hands = reversed(self.hand_values)
			for (hand,tests) in best_hands:
				for t in tests:
					if not t(): break
				else:
					self._value = (self.hand_values.index((hand,tests)),hand)
					break
			return self._value
	def get_cards(self):
		return self._originals

def winning_hand(*hands):
	'''
	compare objects of class poker hand and return winning hand(s)
	problem 54
	'''
	def high_cards(hands):
		highest_value = 0
		winning_hands = set()
		for h in hands:
			high_val = h.get_high_card()
			if high_val > highest_value:
				highest_value,winning_hands = high_val,{h}
			elif high_val == highest_value:
				winning_hands.add(h)
		if len(winning_hands) == 1: return winning_hands
		try:
			return high_cards(winning_hands)
		except StopIteration as e:
			return winning_hands

	winning_val = (0,)
	winning_hands = set()
	for h in hands:
		this_val = h.get_hand_value()
		if  this_val[0] > winning_val[0]:
			winning_hands,winning_val = {h},this_val
		elif this_val[0] == winning_val[0]:
			winning_hands.add(h)
	if len(winning_hands) == 1: return winning_hands
	return high_cards(winning_hands)

def flea_circus(fleas):
	'''
	naive approach
	given 900 randomly jumping fleas originally distributed over a 30 by 30 grid, how many empty squares are expected to be left 
	problem 213
	'''
	for i in range(0,50):
		for v,(x,y) in enumerate(fleas):
			options = []
			if x != 0: options.append((x-1,y))
			if y != 0: options.append((x,y-1))
			if x != 29: options.append((x+1,y))
			if y != 29: options.append((x,y+1))
			fleas[v] = random.choice(options)
	grid = set()
	for xy in fleas:
		grid.add(xy)
	return 900-len(grid)

def flea_position(coords,n = 50):
	'''
	Find the probability of all end points for a flea beginning at grid position x,y after n jumps  
	problem 213
	'''
	x,y = coords
	matrix = collections.defaultdict(float)
	matrix[(x,y)] = 1		
	for i in range(0,n):
		new_matrix = collections.defaultdict(float)
		for (x,y),v in matrix.items():	
			options = []
			if x != 0: options.append((x-1,y))
			if y != 0: options.append((x,y-1))
			if x != 29: options.append((x+1,y))
			if y != 29: options.append((x,y+1))
			new_prob = v*(1/len(options))		
			for (a,b) in options:
				new_matrix[(a,b)] += new_prob
		matrix = new_matrix
        return matrix

def full_matrix():
	'''
	Using resultant flea_positions, find the probability that any given square will be empty
	problem 213
	'''
	x,y = 30,30
	full_matrix = {(i,j):1 for i in range(0,x) for j in range (0,y)}
	for i in range(0,x):
		for j in range(0,y):
			result = flea_position((i,j))
			for (a,b),v in result.items():
				full_matrix[(a,b)] *= 1-v
	return full_matrix

def find_x_less_half_n(n,y):
	return ((n**2)/2 - (y-n/2)**2)**.5

def integer_points_on_a_circle(n):
	results = 0
	for y in range(n+1,int((n/2) + n*(2**.5))+1):
		pos_neg = find_x_less_half_n(n,y)
		try:
			if pos_neg == int(pos_neg): results += 2
		except TypeError:
			continue
	return results*4 + 4

def points_of_reflection(a_x = 0,a_y = 10.1,b_x=1.4,b_y=-9.6):
	'''
	problem 144
	'''
	points = []
	while b_x < -0.01 or b_x > 0.01 or b_y < 0:
		ab_slope = (b_y - a_y)/(b_x - a_x) #slope of incoming line AB
		points.append((b_x,b_y)) #current reflection at bx,by
		tang_slope = -4*b_x/b_y #slope of tang at bx,by

		#find bc slope (angle of reflection)
		trig_ident = (ab_slope - tang_slope)/(1+ab_slope*tang_slope)
		bc_slope = (tang_slope - trig_ident) / (1+trig_ident*tang_slope) #trig identities (slope = tan) gives us outgoing bc_slope
		
		#use bc_slope to find new points cx,cy
		bc_intercept = b_y-(bc_slope*b_x) #use known points on BC (bx,by) and slope BC to solve b = y-mx
		new_xs = solve_quadratic(4+bc_slope*bc_slope,2*bc_intercept*bc_slope,bc_intercept*bc_intercept-100) #find intersection by plugging values into equation for ellipse
		c_x = new_xs[0] if abs(b_x-new_xs[0]) > abs(b_x-new_xs[1]) else new_xs[1] #pick value which is not current one 
		
		#move everything along (b_y = mx+b or b_slope*c_x+intercept)
		a_x,a_y,b_x,b_y = b_x,b_y,c_x,bc_slope*c_x + bc_intercept
	return points

def cyclicate_figural_numbers():
	'''
	problem 61
	'''
	funcs = {lambda n:int(n*(n+1)/2),
				lambda n:n*n,
				lambda n:int(n*(3*n-1)/2),
				lambda n:n*(2*n-1),
				lambda n:int(n*(5*n-3)/2),
				lambda n:n*(3*n-2)}
	terms = []

	for tag,f in enumerate(funcs):
		gen = (f(i) for i in range(1,1000))
		x = next(gen)
		while x < 1000: x = next(gen)
		else:
			while x < 10000:
				terms.append((str(x),tag))
				x = next(gen)

	sequences = [[x,[tag]] for x,tag in terms]

	for term,tag in terms:
		start,end = term[:2],term[2:]
		newly_found = []
		for string,tags in sequences:
			if tag not in tags:
				if string[-2:] == start:
					if end == string[:2] and len(tags+[tag]) == 6: 
						final = string+term
						return [int(final[i:i+4]) for i in range(0,len(final),4)]
					newly_found.append((string+term,tags+[tag]))
				elif string[:2] == end:
					newly_found.append((term+string,tags+[tag]))
		sequences.extend(newly_found)

def get_minimal_diophantine_quadratic(d):
	if d**.5 == int(d**.5): raise ValueError
	y = 1
	x_sq = d*(y**2)+1
	while x_sq**.5 != int(x_sq**.5):
		y += 1
		x_sq = d*(y**2)+1
	return (int(x_sq**.5),y)

def diophantine_maximum_minimal_solutions(minimum=1,maximum = 1000,limit=5):
	ds = {d:False for d in range(minimum,maximum+1) if d**.5 != int(d**.5)}
	y = 0
	while len(ds) > limit:
		y += 1
		for d in ds:
			if d != False: 
				continue
			x_sq = d*(y**2)+1
			if int(x_sq**.5) == x_sq**.5: 
				ds[d] = (int(x_sq**.5),y)
		ds = {d:False for d,v in ds.items() if v == False}
	return ds 

def singular_integer_right_triangles(limit=1500000):
	'''
	problem 75
	'''
	from fractions import gcd
	def has_triple(p):
		m_max = int(p**.5)
		m_min = int(max(solve_quadratic(2,-1,-p)))
		for m in range(m_min,m_max+1):
			for n in range(1 if m % 2 == 0 else 2,m,2):
				if gcd(m,n) > 1: continue
				if m*(m+n) == p: return 1
		return 0

	internal_limit = int(limit/2)+1
	perimeters = {p:0 for p in range(5,internal_limit)}
	for p,num in perimeters.items():
		if num != 0:
			continue
		if has_triple(p):
			for x in range(p,internal_limit,p): perimeters[x] = 1 if perimeters[x] == 0 else -1
	return perimeters

def singular_pythagorean_triple(limit = 1500000):
	'''
	problem 75
	'''
	from fractions import gcd
	internal_limit = int(limit/2)
	perimeters = [0]*internal_limit
	for m in range(2,int(internal_limit**.5)+1):
		for n in range(1 if m % 2 == 0 else 2,m,2):
			if gcd(m,n) == 1:
				p = m*(m+n)
				for x in range(p,internal_limit,p): perimeters[x] += 1
	return perimeters.count(1)

def coprime_pair_generator(maximum):
	last_coprimes = {(2,1)}
	while last_coprimes:
		new_coprimes = set()
		for a,b in last_coprimes:
			yield (a,b)
			new_coprimes.update((c,d) for c,d in ((2*a-b,a),(2*a+b,a),(a+2*b,b)) if c < maximum)
		last_coprimes = new_coprimes

def pythagorean_triples(limit = 1500000):
	'''
	problem 75
	'''
	internal_limit = int(limit/2)
	perimeters = [0]*internal_limit
	for m,n in coprime_pair_generator(internal_limit**.5):
		p = m*(m+n)
		for x in range(p,internal_limit,p): perimeters[x] += 1
	return perimeters.count(1)

def final_test(limit = 1500000):
	internal_limit = int(limit/2)
	perimeters = [0]*internal_limit
	m_max = internal_limit**.5
	def branch(m, n):
		if m < m_max:
			p = m*(m+n)
			for x in range(p,internal_limit,p): perimeters[x] += 1
			branch(2*m - n, m)
			branch(2*m + n, m)
			branch(m + 2*n, n)
	branch(2, 1)
	return perimeters.count(1)

def bouncy_number_percent(percent = 50):
	def is_increasing(s):
		for i in range(0,len(s)-1):
			if s[i] > s[i+1]:
				return False
		return True

	def is_decreasing(s):
		for i in range(0,len(s)-1):
			if s[i] < s[i+1]:
				return False
		return True

	bouncy = 0
	i = 100
	while i < 200:
		i += 1
		s = str(i)
		if is_increasing(s):
			print(i,' is increasing')
		elif is_decreasing(s):
			print(i,' is decreasing')
		else:
			print(i,' is bouncy')

def rectangular_grids(target = 2000000):
	grid_sums,rectangles = {}, {}
	for g_width in range(1,100):
		for g_height in range(1,g_width+1):
			num, r_width = 0, g_width
			while r_width > 0:
				r_height = g_height
				while r_height > 0:
					width_wise,height_wise = g_width-r_width+1,g_height-r_height+1
					num += width_wise*height_wise
					r_height -= 1
				r_width -= 1
			grid_sums[(g_width,g_height)] = num
	return grid_sums

def concealed_square():
	min_num,max_num = 1010101000,int(int('9'.join(str(i) for i in [i for i in range(1,10)]+[0]))**.5)
	digit_positions = sorted(((i,v) for i,v in enumerate('1_2_3_4_5_6_7_8_9_0') if v != '_'),reverse=True)
	for i in range(max_num,min_num,10):
		if i % 3 != 0 or i % 7 != 0: continue
		squared = str(i*i)
		if all(v == squared[d] for d,v in digit_positions): return i

def spec_cross_product(a,b):
	return (-a[0])*(b[1]-a[1])-(-a[1])*(b[0]-a[0]) > 0

def origin_within_triangle(v0,v1,v2):
	return spec_cross_product(v0,v1) == spec_cross_product(v1,v2) == spec_cross_product(v2,v0)

class Monopoly:
	'''
	class finding the probabilities of a Monopoly turn ending on every square for given dice (through simulation)
	problem 84
	'''
	def __init__(self,dice):
		'''
		requires dice passed (see helper function get_n_sided_dice), designates spots w/ special actions, 
		creates lambdas expecting current position for every significant card
		'''
		self._cc_squares,self._ch_squares = {2,17,33}, {7,22,36}

		cc_cards = [lambda x,tar=tar:tar for tar in ['STAY']*14+[0,10]] #where the cc cards point
		random.shuffle(cc_cards)
		self._cc_cards = itertools.cycle(cc_cards) #itertools is awesome

		ch_cards = [lambda x,tar=tar:tar for tar in ['STAY']*6+[0,10,11,24,39,5]] #where the chance cards point
		next_rr = lambda x: {7:15,22:25,36:5}[x] #go to next railroad
		ch_cards.extend([next_rr,next_rr,lambda x: {7:12,22:28,36:12}[x],lambda x: x-3]) # next rr *2, next utility, go back 3 
		random.shuffle(ch_cards)
		self._ch_cards = itertools.cycle(ch_cards) 

		self._dice, self._doubles_counter = dice, 0 

		self._current_position, self.end_positions = 0, collections.defaultdict(int)

	def play_turn(self):
		"only real interface with logic (makes sense -- neutered form of Monopoly might as well be Candyland, no decisions to be made)"
		roll = [random.choice(d) for d in self._dice]

		roll_target = None
		self._doubles_counter = 0 if not all(d == roll[0] for d in roll) else self._doubles_counter + 1  #checks for doubles, safe for 2+ dice, not for 1 die (feels silly to check length every time)
		if self._doubles_counter == 3: #checks for three doubles go to jail rule (would be fun to generalize for house rules)
			self._doubles_counter, roll_target = 0, 10 # go to jail
		else:
			new_spot = sum(roll)+self._current_position
			roll_target = new_spot if new_spot < 40 else new_spot-40 #this is the only place where 39-to-0 wrap around can happen, so address it here

		self._current_position = self._parse_move(roll_target) #pass dice roll to parse_move, save as current position
		self.end_positions[self._current_position] += 1 #tally current position

	def _parse_move(self,move):
		'''
		Where the action is. Recurses until a move isn't a chance or cc card requiring movement
		'''
		if move in self._cc_squares:
			result = next(self._cc_cards)(move) #calling returned lambda with argument of move (integer representing position)
		elif move in self._ch_squares:
			result = next(self._ch_cards)(move) #ditto
		elif move == 30: return 10 #go to jail square
		else: return move #if here, then move was just a regular old move
		return move if result == 'STAY' else self._parse_move(result) #Only CC and CH cards at this point; recursion if they don't have an action

	def print_end_position_percents(self):
		'''
		helper function prints results pretty-like
		'''
		total_moves = sum(self.end_positions.values())
		print('Total moves: ',total_moves)
		for i,v in sorted(self.end_positions.items(),key=lambda x:x[1],reverse=True):
			print(i,' ',100*v/total_moves,'%')

	def get_n_sided_dice(n,s=2):
		'''
		generate s dice-tuples with n sides (not actual method, doesn't need self argument)
		'''
		if s < 2:
			raise ValueError('Monopoly can only be played with two or more dice.') #doubles rule will break if less than s
		return tuple(tuple(i for i in range(1,n+1)) for j in range(0,s))	

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

def permuted_totients(limit=10**7):
	'''
	problem 70 -- find the permuted number-totient pair for which n/phi(n) is a minimum
	'''
	rooted = int((limit)**.5)
	primes = get_all_primes_under(rooted*3)
	mid_index = primes.index(min(primes,key=lambda x:abs(x-rooted)))
	step = mid_index//10
	best_n_phi, found, i, cache = limit, (0,0,0), 0, set()
	while found == (0,0,0) and i < mid_index:
		i += step
		for p in primes[mid_index:mid_index+i]:
			for q in primes[mid_index:mid_index-i:-1]:
				n = p*q
				if n > limit or n in cache: continue
				cache.add(n)
				phi = (p-1)*(q-1)
				n_over_phi = n/phi
				if n_over_phi > best_n_phi: break
				sn,sphi = str(n),str(phi)
				if sorted(sn) == sorted(sphi):
					best_n_phi,found = n_over_phi,(n,p,q)
					break #if we find one here, we won't find any better totient ratios below, so stop looking
	return found

def counting_fractions(limit=1000001):
	'''
	how many proper reduced fractions are there with a denominator less than the given limit
	problem 72
	'''
	t = Totient(limit)
	return sum(t.totients)-2

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

def odd_periods_of_continued_fractions_under(limit = 10000):
	'''
	problem 64
	'''
	count = 0
	for i in range(2,limit+1):
		if i**.5 == int(i**.5): continue
		fracs = continued_fraction_of_root(i)
		if (len(fracs) - 1) % 2 == 1:
			count += 1
	return count

def dijkstra(graph,source,target,neighbor_func,distance_func):
	infinity = float('inf')
	unvisited,distances,previous = {n for n in graph},collections.defaultdict(lambda : infinity),collections.defaultdict(lambda : None)		
	distances[source] = 0
	while unvisited:
		current = min(unvisited.intersection(distances),key=lambda x:distances[x])
		unvisited.remove(current)
		if distances[current] == infinity:
			break
		for n in neighbor_func(current):
			if n not in unvisited:
				continue
			alt = distances[current] + distance_func(current,n)
			if alt < distances[n]:
				distances[n],previous[n] = alt, current
	if not target:
		return previous
	s,u = [],target
	while previous[u]:
		s.append(u)
		u = previous[u]
	s.reverse()
	return tuple([source]+s)

def three_way_path_sum(matrix):
	'''
	problem 82
	'''
	dimension = max(matrix)[0]

	@memo
	def neighbor_function(node):
		neighbors = set()
		a,b = node
		if a+1 <= dimension: neighbors.add((a+1,b))
		if b-1 >= 0: neighbors.add((a,b-1))
		if b+1 <= dimension: neighbors.add((a,b+1))
		return neighbors

	minimum, min_path, targets = float('inf'), None, tuple((dimension,i) for i in range(dimension))
	for j in range(dimension):
		source = (0,j)
		previous,paths = dijkstra(matrix.keys(),source,None,neighbor_function,lambda x,y:matrix[y]),set()
		for a in targets:
			if a not in previous or previous[a] in targets:
				continue
			b,s = a,[]
			while previous[b]:
				s.append(previous[b])
				if previous[b] == source:
					break
				b = previous[b]
			else:
				continue
			s.reverse()
			paths.add(tuple(s+[a]))
		path_sums = {path:sum(matrix[p] for p in path) for path in paths}
		this_min = min(path_sums.items(),key=lambda x: x[1])
		if this_min[1] < minimum:
			min_path,minimum = this_min
	return minimum,min_path

def four_way_path_sum(matrix):
	'''
	problem 83
	'''
	dimension = max(matrix)[0]

	@memo
	def neighbor_function(node):
		neighbors = set()
		a,b = node
		if a+1 <= dimension: neighbors.add((a+1,b))
		if a-1 >= 0: neighbors.add((a-1,b))
		if b-1 >= 0: neighbors.add((a,b-1))
		if b+1 <= dimension: neighbors.add((a,b+1))
		return neighbors

	def distance_func(first,next):
		return matrix[next]

	min_path = dijkstra(matrix.keys(),(0,0),(dimension,dimension),neighbor_function,distance_func)
	value = sum(matrix[a,b] for a,b in min_path)
	return min_path,value

test_matrix = {
			(0,0):131,(0,1):201,(0,2):630,(0,3):537,(0,4):805,
			(1,0):673,(1,1):96,(1,2):803,(1,3):699,(1,4):732,
			(2,0):234,(2,1):342,(2,2):746,(2,3):497,(2,4):524,
			(3,0):103,(3,1):965,(3,2):422,(3,3):121,(3,4):37,
			(4,0):18,(4,1):150,(4,2):111,(4,3):956,(4,4):331}

def prime_summations(n):
	'''
	problem 77
	'''
	prime_sums, primes = {0:1,1:0}, []
	for i in range(2,n):
		if is_prime(i): 
			primes.append(i)

	return prime_sums

def find_pandigital_fib():
	def fib_gen_last_nine():
		a,b = 0,1
		while True:
			yield a
			a,b = b,(a+b)%10**9	
	
	log_root_five, log_phi = math.log(5**.5,10), math.log((1+5**.5)/2,10)
	def fib_first_nine(n):
		product = n*log_phi-log_root_five
		return int(10**(product-int(product)+8))
	@memo
	def is_pandigital(string):
		return True if len(set(string)) == 9 and '0' not in string else False
	
	fib = fib_gen_last_nine()
	f,i = next(fib),0
	while not is_pandigital(str(f)) or not is_pandigital(str(fib_first_nine(i))):
		f,i = next(fib),i+1
	return f,i

def word_square_anagrams(words):
	'''
	problem 95
	'''
	squares = (str(i*i) for i in range(1,int(999999999**.5) + 1))

	def map_to_digits(w_pair):
		a,b = w_pair
		j = 0
		for i in range(len(a)):
			z = a[i]
			if z.isdigit(): continue
			k = str(j)
			a,b = a.replace(z,k), b.replace(z,k)
			j += 1
		return a,b
	def map_to_chars_to_digits(sq_pair):
		a,b = sq_pair
		return map_to_digits(tuple(''.join([chr(int(s) + 64) for s in sq]) for sq in sq_pair))

	def add_to_anagrams(items,mapping_func):
		anagrams = collections.defaultdict(set)
		sqs_or_ws = collections.defaultdict(set)
		for item in items:
			if is_palindrome(item): continue
			sqs_or_ws[tuple(sorted(item))].add(item)
		for anags in sqs_or_ws.values():
			if len(anags) < 2: continue
			for pair in itertools.combinations(anags,2):
				anagrams[mapping_func(pair)].add(pair)
		return anagrams

	w_grams, sq_grams = add_to_anagrams(words,map_to_digits), add_to_anagrams(squares,map_to_chars_to_digits)
	maximum = 0
	max_info = None
	for pair_key in w_grams:
		if pair_key in sq_grams:
			sq_pairs = {(int(a),int(b)) for a,b in sq_grams[pair_key]}
			c = max(sq_pairs,key=lambda x:max(x))
			if max(c) > maximum: 
				maximum = max(c)
				max_info = c,w_grams[pair_key]
	return maximum,max_info

def fizzBuzz():
	'''
	print fizz for multiples of 3, buzz for multiples of 5, the number for everything else.
	'''
	for i in range(1,101):
		if i % 3 == 0 and i % 5 == 0: print('FizzBuzz') #clearer than % 15 ?
		elif i % 3 == 0: print('Fizz')
		elif i % 5 == 0: print('Buzz')
		else: print(i)

def binomial_coefficient(n,k):
	return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def dice_roll_odds(p,n,s):
	return (1/s**n)*sum((-1)**k*binomial_coefficient(n,k)*binomial_coefficient(p-s*k-1,n-1) for k in range(0,int((p-n)/s)+1))

# def convergents(n):
# 	r,i = n,int(n)
# 	parts = []
# 	while r!= 0:
# 		parts.append(i)
# 		yield convergent_from_continued_fraction(parts)
# 		f = 1/(r-i)
# 		r,i = f,int(f)

# def convergent_from_continued_fraction(parts):
# 	x = 0
# 	for i in range(len(parts)-1,0,-1):
# 		x = fractions.Fraction(1,parts[i]+x)
# 	return fractions.Fraction(parts[0]+x)

def continued_fraction_of_root(n):
	'''
	problem 64
	'''
	root_n = n**.5
	m,d,a = 0,1,int(root_n)
	continued_fracs = []
	while (m,d,a) not in continued_fracs:
		continued_fracs.append((m,d,a))
		m = int(d*a-m)
		d = int((n-m**2)/d)
		a = int((root_n+m)/d)
	return continued_fracs

def diophantine(D):
	rooted = int(D**.5)
	m,d,a = 0,1,rooted
	p,q = [0,1,a],[1,0,1]
	while True:
		m = d*a-m
		d = (D-m**2)/ d
		a = (rooted+m)/d
		p.append(a*p[-1]+p[-2])
		q.append(a*q[-1]+q[-2])
		yield p[-1]

def make_sudoku_grids():
	import csv
	sudokus = []
	with open('lib/sudoku.txt') as csvfile:
		sudoku_grids = csv.reader(csvfile)
		while True:
			try:
				next(sudoku_grids)
				sudokus.append([i for i in itertools.islice(sudoku_grids,9)])
			except StopIteration:
				break
	new_sudokus = []
	for s in sudokus:
		new_s = {}
		for x,row in enumerate(s):
			for y,val in enumerate(row[0]):
				new_s[(x,y)] = {int(val)}
		new_sudokus.append(new_s)
	return new_sudokus

def print_sudoku(grid):
	for x in range(0,9):
		row = ''
		for y in range(0,9):
			current = grid[x,y]
			if len(current) > 1 or current == {0}:
				row += '{ } ';
			else:
				row += str(grid[(x,y)])+' '
		print(row)

def order_radicals_under(limit = 10):
	sieve = [1]*(limit+1)
	for i in range(2,limit+1):
		if sieve[i] == 1:
			for j in range(i,limit+1,i):
				sieve[j] *= i
	return sorted(((i,v) for i,v in enumerate(sieve)),key=lambda x:(x[1],x[0]))

def integer_right_triangles(limit=50):
	'''
	either hypotenuse / height have to be integer, or a and b have to be 
	'''
	origin = (0,0)
	triangles = set()
	points = set((x,y) for x in range(limit+1) for y in range(limit+1))
	points.remove(origin)
	for x,y in points:
		if x == 0:
			p_points = {(p_x,y) for p_x in range(limit+1)}
			p_points.update(((0,p_y) for p_y in range(limit+1)))
		elif y == 0:
			p_points = {(x,p_y) for p_y in range(limit+1)}
			p_points.update(((p_x,0) for p_x in range(limit+1)))
		else:
			gcdxy, p_points = fractions.gcd(x,y), set()
			dx,dy = x//gcdxy, y//gcdxy

			up_x,up_y = x-dx,y+dy
			while up_y <= limit and up_x >= 0:
				p_points.add((up_x,up_y))
				up_x,up_y = up_x-dx,up_y+dy

			down_x,down_y = x+dx,y-dy
			while down_y >= 0 and down_x <= limit:
				p_points.add((down_x,down_y))
				down_x,down_y = down_x+dx,down_y-dy

		for p_x,p_y in p_points:
			if p_x == x and p_y == y or (p_x,p_y) == origin: continue
			if p_y > y:
				triangles.add((origin,(p_x,p_y),(x,y)))
			else:
				triangles.add((origin,(x,y),(p_x,p_y)))		
	return triangles

def consecutive_divisors(limit):
	numbers = [{1} for i in range(limit+1)]
	numbers[0] = set()
	consecutive = 0
	for i in range(2,limit+1):
		for j in range(i,limit+1,i):
			numbers[j].add(i)
		if len(numbers[i]) == len(numbers[i-1]):
			consecutive += 1
	return consecutive

def laminae(limit = 100):
	max_d = int(max(solve_quadratic(1,2,-limit)))
	return sum(int((limit+d)**2/(2*d))-d for d in range(2,max_d+1,2))

def semiprimes(limit = 30):
	found, sieve = 0, [0 for i in range(limit+1)]
	for i in range(2,limit+1):
		if sieve[i] == 2: 
			found += 1
		if sieve[i] != 0:
			continue
		sqed = i**2
		for j in range(i,limit+1,i):
			if j % sqed == 0:
				if j == sqed: 
					sieve[j] += 2
				else:
					sieve[j] += 3
			else:
				sieve[j] += 1
	return found,sieve

class sudoku_grid():
	def __init__(self,grid):
		self._grid = grid
		self._map = {(x,y):{d for d in range(1,10)} for x in range(0,9) for y in range(0,9)}
		self._incomplete = set(self._map.keys())
		for (x,y),value in self._grid.items():
			if value != {0}:
				self._map[x,y] = value
				self._distribute((x,y))
	
	def _diff(self,target,cell):
		if self._map[target].intersection(self._map[cell]):
			self._map[target].difference_update(self._map[cell])
			self._distribute(target)

	def _distribute(self,cell): #only call after cell's value has been changed
		values = self._map[cell]
		length = len(values)
		if length == 1:
			self._incomplete.discard(cell)
			for d in self._dependents(cell):
				self._diff(d,cell)
		else:
			for group in (set(g(cell)) for g in (self._row,self._col,self._box)):
				if length == 1+sum(1 for other in group if values == self._map[other]): #if {1,2},{1,2},{1,2,3}, then {1,2},{1,2},{3}
					for target in group:
						if self._map[target] != values: 
							self._diff(target,cell)

	def _check_for_unique(self,group):
		for d in range(1,10):
			cells_with_d = [g for g in group if d in self._map[g]]
			if len(cells_with_d) == 1:
				for cell_with_d in cells_with_d:
					if len(self._map[cell_with_d]) != 1:
						self._map[cell_with_d] = {d}
						self._distribute(cell_with_d)

	def _dependents(self,cell):
		return itertools.chain(self._row(cell),self._col(cell),self._box(cell))

	def _row(self,cell):
		return ((d,cell[1]) for d in range(0,9) if d != cell[0])

	def _col(self,cell):
		return ((cell[0],d) for d in range(0,9) if d != cell[1])

	def _box(self,cell):
		box_x,box_y = (cell[0]//3)*3,(cell[1]//3)*3
		return  ((a,b) for a in range(box_x,box_x+3) for b in range(box_y,box_y+3) if (a,b) != cell)

	def _get_groups(self):
		reps = ((0,0),(3,1),(6,2),(1,3),(4,4),(7,5),(2,6),(5,7),(8,8))
		for method in (self._row,self._col,self._box):
			for cell in reps:
				yield {c for c in method(cell)}|{cell}
		
	def get_solution(self):		
		for group in self._get_groups():
			self._check_for_unique(group)
		if not self._incomplete:
			#need cocde to start testing hypotheticals
			pass
	
