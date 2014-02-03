from functools import reduce
from operator import mul


product = lambda nums: reduce(mul, nums)
