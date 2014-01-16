

def sum_multiples_of_three_and_five(limit=1000):
    return sum(x for x in xrange(limit) if x % 3 == 0 or x % 5 == 0)


if __name__ == '__main__':
    print sum_multiples_of_three_and_five()
