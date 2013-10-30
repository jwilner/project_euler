from itertools import takewhile,cycle,count
from problem_44 import pentagon_gen

def partition(n):
    '''
    find the lowest integer for which the number
    of its partitions is a multiple of 1,000,000
    problem 78
    '''
    partitions = {}
    generalized_pentagonals = sorted([i for i in pentagon_gen(-250,250)])[1:]
    def part(n):
        if n <= 1: return 1
        if n not in partitions:
            signs = cycle([1,1,-1,-1])
            pentagonals = takewhile(lambda p:p <= n, generalized_pentagonals)
            partitions[n] = sum(sign*part(n-p) for sign,p in zip(signs,pentagonals))
        return partitions[n]
    return part(n)
