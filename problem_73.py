from fractions import Fraction,gcd
import math

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


