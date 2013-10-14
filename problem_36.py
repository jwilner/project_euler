
def is_palindrome(n):
	'''
	returns true or false depending on whether input string is palindromic
	problems 36, 55
	'''
	if type(n) != str:
		raise TypeError
	return True if n == n[::-1] else False


