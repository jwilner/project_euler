
class triangleNumbers:
'''
for dealing with triangle numbers
problem 12
'''
    def __init__(self):
        self.cache = {1 : 1}

    def get_nth_triangle_number(self,n):
        '''finds the nth triangle number'''
        if n in self.cache:
            return self.cache[n]
        new_val = (n*(n+1))/2
        self.cache[n] = new_val
        return new_val
    def get_first_triangle_number_with_n_factors(self,n):
        '''
        returns the position of the first triangle number
         with at least n factors'''
        i = 1
        num_factors = 1
        while num_factors < n:
            i = i + 1
            factors = factorNumber(self.getNthTriangleNumber(i))
            num_factors = len(factors)
        return (i,num_factors)
