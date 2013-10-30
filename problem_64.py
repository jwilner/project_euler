
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


