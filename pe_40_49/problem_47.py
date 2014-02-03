from utils import prime_factors
import collections

def numbers_with_n_distinct_factors(num_distinct = 4):
    '''
    Find the first four integers each with four distinct prime factors
    problem 47
    '''
    Counter = collections.Counter
    number_factors = [[],[]]
    for i in range(2,1000000):
        first = [i**v for i,v in Counter(prime_factors(i)).items()]
        number_factors.append(first)
        if len(first) >= num_distinct:
            test_set = set(first)
            b = number_factors[-num_distinct:-1]
            expected = num_distinct * 2
            for c in b[::-1]:
                test_set.update(c)
                if len(test_set) < expected:
                    break
                expected += num_distinct
            else:
                return number_factors[-num_distinct:]
