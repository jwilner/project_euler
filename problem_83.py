from utils import memo, dijkstra

def four_way_path_sum(matrix):
	'''
	problem 83
	'''
	dimension = max(matrix)[0]

	@memo
	def neighbor_function(node):
		neighbors = set()
		a,b = node
		if a+1 <= dimension: neighbors.add((a+1,b))
		if a-1 >= 0: neighbors.add((a-1,b))
		if b-1 >= 0: neighbors.add((a,b-1))
		if b+1 <= dimension: neighbors.add((a,b+1))
		return neighbors

	def distance_func(first,next):
		return matrix[next]

	min_path = dijkstra(matrix.keys(),(0,0),(dimension,dimension),neighbor_function,distance_func)
	value = sum(matrix[a,b] for a,b in min_path)
	return min_path,value

test_matrix = {
			(0,0):131,(0,1):201,(0,2):630,(0,3):537,(0,4):805,
			(1,0):673,(1,1):96,(1,2):803,(1,3):699,(1,4):732,
			(2,0):234,(2,1):342,(2,2):746,(2,3):497,(2,4):524,
			(3,0):103,(3,1):965,(3,2):422,(3,3):121,(3,4):37,
			(4,0):18,(4,1):150,(4,2):111,(4,3):956,(4,4):331}


