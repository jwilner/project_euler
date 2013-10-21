
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


