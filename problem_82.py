from utils import dijkstra, memo

def three_way_path_sum(matrix):
	'''
	problem 82
	'''
	dimension = max(matrix)[0]

	@memo
	def neighbor_function(node):
		neighbors = set()
		a,b = node
		if a+1 <= dimension: neighbors.add((a+1,b))
		if b-1 >= 0: neighbors.add((a,b-1))
		if b+1 <= dimension: neighbors.add((a,b+1))
		return neighbors

	minimum, min_path, targets = float('inf'), None, tuple((dimension,i) for i in range(dimension))
	for j in range(dimension):
		source = (0,j)
		previous,paths = dijkstra(matrix.keys(),source,None,neighbor_function,lambda x,y:matrix[y]),set()
		for a in targets:
			if a not in previous or previous[a] in targets:
				continue
			b,s = a,[]
			while previous[b]:
				s.append(previous[b])
				if previous[b] == source:
					break
				b = previous[b]
			else:
				continue
			s.reverse()
			paths.add(tuple(s+[a]))
		path_sums = {path:sum(matrix[p] for p in path) for path in paths}
		this_min = min(path_sums.items(),key=lambda x: x[1])
		if this_min[1] < minimum:
			min_path,minimum = this_min
	return minimum,min_path


