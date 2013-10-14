
def count_coins(coins = [1,2,5,10,20,50,100,200],value=200):
	table = [0 for x in range(value + 1)]
	m = len(coins)
	table[0] = 1
	for i in range(0,m):
		for j in range(coins[i],value+1):
			table[j] += table[j-coins[i]]
	return table[value]

