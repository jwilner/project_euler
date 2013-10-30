import itertools, collections
from utils import is_palindrome

def word_square_anagrams(words):
	'''
	problem 95
	'''
	squares = (str(i*i) for i in range(1,int(999999999**.5) + 1))

	def map_to_digits(w_pair):
		a,b = w_pair
		j = 0
		for i in range(len(a)):
			z = a[i]
			if z.isdigit(): continue
			k = str(j)
			a,b = a.replace(z,k), b.replace(z,k)
			j += 1
		return a,b
	def map_to_chars_to_digits(sq_pair):
		a,b = sq_pair
		return map_to_digits(tuple(''.join([chr(int(s) + 64) for s in sq]) for sq in sq_pair))

	def add_to_anagrams(items,mapping_func):
		anagrams = collections.defaultdict(set)
		sqs_or_ws = collections.defaultdict(set)
		for item in items:
			if is_palindrome(item): continue
			sqs_or_ws[tuple(sorted(item))].add(item)
		for anags in sqs_or_ws.values():
			if len(anags) < 2: continue
			for pair in itertools.combinations(anags,2):
				anagrams[mapping_func(pair)].add(pair)
		return anagrams

	w_grams, sq_grams = add_to_anagrams(words,map_to_digits), add_to_anagrams(squares,map_to_chars_to_digits)
	maximum = 0
	max_info = None
	for pair_key in w_grams:
		if pair_key in sq_grams:
			sq_pairs = {(int(a),int(b)) for a,b in sq_grams[pair_key]}
			c = max(sq_pairs,key=lambda x:max(x))
			if max(c) > maximum: 
				maximum = max(c)
				max_info = c,w_grams[pair_key]
	return maximum,max_info


