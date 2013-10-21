from math import factorial

def digit_factorials(limit = 1000):
	'''
	Digit factorial chains tend to repeat. Return the length of repeating chains under a given limit
	problem 74
	'''	
	#in loop 654321321, 6,5,4 would have 6,5,4 'non-repeating' numbers, but 3,2,1 would each have 3, because they occur w/in loop

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


