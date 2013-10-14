
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


