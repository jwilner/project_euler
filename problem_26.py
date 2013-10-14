import itertools

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


