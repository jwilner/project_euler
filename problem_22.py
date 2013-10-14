
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


