import itertools

def pandigital_products():
    '''
    find all products whose producing equation has every digit 1 to 9 inclusive once; e.g. 39 x 186 = 7254
    problem 32
    '''
    possibilities = itertools.permutations(str(i) for i in range(1,10))
    identities  = [(int(''.join(x[5:])),x[:5]) for x in possibilities]
    return {p for p,x in identities if int(''.join(x[:2]))*int(''.join(x[2:]))==p or int(''.join(x[:1]))*int(''.join(x[1:])) == p}
