import math

def binomial_coefficient(n,k):
	return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def dice_roll_odds(p,n,s):
	return (1/s**n)*sum((-1)**k*binomial_coefficient(n,k)*binomial_coefficient(p-s*k-1,n-1) for k in range(0,int((p-n)/s)+1))


