
def bouncy_number_percent(percent = 50):
	def is_increasing(s):
		for i in range(0,len(s)-1):
			if s[i] > s[i+1]:
				return False
		return True

	def is_decreasing(s):
		for i in range(0,len(s)-1):
			if s[i] < s[i+1]:
				return False
		return True

	i = 100
	while i < 200:
		i += 1
		s = str(i)
		if is_increasing(s):
			print(i,' is increasing')
		elif is_decreasing(s):
			print(i,' is decreasing')
		else:
			print(i,' is bouncy')


