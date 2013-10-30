
def get_minimal_diophantine_quadratic(d):
	if d**.5 == int(d**.5): raise ValueError
	y = 1
	x_sq = d*(y**2)+1
	while x_sq**.5 != int(x_sq**.5):
		y += 1
		x_sq = d*(y**2)+1
	return (int(x_sq**.5),y)

def diophantine_maximum_minimal_solutions(minimum=1,maximum = 1000,limit=5):
	ds = {d:False for d in range(minimum,maximum+1) if d**.5 != int(d**.5)}
	y = 0
	while len(ds) > limit:
		y += 1
		for d in ds:
			if d != False: 
				continue
			x_sq = d*(y**2)+1
			if int(x_sq**.5) == x_sq**.5: 
				ds[d] = (int(x_sq**.5),y)
		ds = {d:False for d,v in ds.items() if v == False}
	return ds 


