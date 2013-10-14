
def pandigital_multiples(digits = 9):
	'''
	find the largest pandigital 1 to digits number that can be formed by concatenating the products of n and each of {1,2 ... i}
	problem 38
	'''
	max_length = 4
	biggest = 0
	previous_biggest = []
	final_chars = set(str(i) for i in range(1,digits+1))
	for i in range(1,10**max_length):
		chars = set()
		strung_num = ''
		nums = []
		m = 0
		while len(strung_num) < digits:
			m += 1
			num = i * m
			# if len(previous_biggest) >= m and num < previous_biggest[m-1]:
			# 	bypass = True
			# 	break
			nums.append(num)
			strung = str(num)
			chars |= set(strung)
			strung_num += strung
			if len(chars) < len(strung_num):
				break
		else:
			number = int(strung_num)
			if chars == final_chars and number > biggest :
				previous_biggest, biggest = nums,number
		if i > 300 and i < 400:
			print(nums)
	return previous_biggest
