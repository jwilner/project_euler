from utils import solve_quadratic

def is_triangle_number(n):
	'''
	tests whether number is a triangle number using quadratic formula
	problem 45
	'''
	roots = solve_quadratic(1,1,-2*n)
	return True if [r for r in roots if r > 0 and r == int(r)] else False

def is_pentagonal_number(n):
	'''
	tests whether number is a pentagonal number using quadratic formula
	problem 45
	'''
	roots = solve_quadratic(3,-1,-2*n)
	return True if [r for r in roots if r > 0 and r == int(r)] else False

def is_hexagonal_number(n):
	'''
	tests whether number is a hexagonal number using quadratic formula
	problem 45
	'''
	roots = solve_quadratic(2,-1,-n)
	return True if [r for r in roots if r > 0 and r == int(r)] else False

def get_nth_hexagonal_number(n):
	'''
	returns the nth item from the hexagonal number sequence (subset of triangle numbers)
	problem 45
	'''
	return 2*(n**2)-n


