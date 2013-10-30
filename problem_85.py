
def rectangular_grids(target = 2000000):
	grid_sums,rectangles = {}, {}
	for g_width in range(1,100):
		for g_height in range(1,g_width+1):
			num, r_width = 0, g_width
			while r_width > 0:
				r_height = g_height
				while r_height > 0:
					width_wise,height_wise = g_width-r_width+1,g_height-r_height+1
					num += width_wise*height_wise
					r_height -= 1
				r_width -= 1
			grid_sums[(g_width,g_height)] = num
	return grid_sums


