import decimal

def digital_sums_of_square_roots(limit = 100):
    '''
    for natural numbers one to limit, find the digital sums of all irrational square roots
    problem 80
    '''
    irrationals = []
    for n in range(1,limit+1):
        rooted = decimal.Decimal(n).sqrt()
        if int(rooted) != rooted:
            irrationals.append(str(int(rooted*10**99)))
    return [sum([int(d) for d in i]) for i in irrationals]
