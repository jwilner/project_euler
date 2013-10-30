import math
from utils import memo

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


