from utils import Totient

def counting_fractions(limit=1000001):
    '''
    how many proper reduced fractions are there with a denominator less than the given limit
    problem 72
    '''
    t = Totient(limit)
    return sum(t.totients)-2
