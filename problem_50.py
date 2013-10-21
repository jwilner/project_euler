from problem_10 import get_all_primes_under
from problem_7 import is_prime

def consecutive_prime_sum(lim = 1000):
	'''
	find the longest sequence of primes summing to a prime beneath lim
	problem 50
	'''
	all_primes = get_all_primes_under(lim)
	longest = {'length':2,'sum':5}
	min_sum = 5
	while longest['length'] < len(all_primes):
		p = all_primes.pop()
		if p < min_sum:
			print('hit min sum ',min_sum)
			break
		med = int(p/2)
		b = min(range(len(all_primes)), key=lambda i: abs(all_primes[i]-med))
		a = b-1
		value = sum(all_primes[a:b+1])
		primes_underneath = sum(all_primes[:a])
		while a > 0:
			if value > p:
				value -= all_primes[b]
				b -= 1
				a -= 1
				value += all_primes[a]
				primes_underneath -= all_primes[a]
			elif value < p:
				if primes_underneath < p-value:
					break
				a -= 1
				value += all_primes[a]
				primes_underneath -= all_primes[a]
			else:
				length = b-a+1
				if length > longest['length']:
					longest['length'],longest['sum'] = length,value
					min_sum = sum(all_primes[:longest['length']])
				value -= all_primes[b]
				b -= 1
	return longest

def alternate_prime_sum():
	ps=get_all_primes_under(3946)
	mt,ms,mcps=len(ps),sum(ps),(0,0)
	while mt>mcps[0]:
	  ls=ms if ms%2 else ms-1
	  while not is_prime(ls): ls-=2
	  k,ts=0,ms
	  while ts-ls>0: ts-=ps[k]; k+=1
	  if ts==ls and mt-k>mcps[0]: mcps=(mt-k,ts)
	  mt-=1
	  ms-=ps[mt]
	    
	print(mcps)

def eul50():
    primes = get_all_primes_under(10**6)
    d = {}
    running = 0
    for p in primes:
        if p > 50000: break
        running += p
        d[p] = running
    b = sorted(d.keys())
    best = (21, 953)
    e = {}
    for i in range(len(b)):
        for j in range(i + (best[0] if best[0]%2 == 1 else best[0]-1), len(b)-1, 2):
            val = d[b[j]] - d[b[i]]
            if val > 1000000: break
            if val in primes and j-i > best[0]: best=(j-i, val)
    return best


