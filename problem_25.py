
def getFirstFibOfLength(digits):
    '''
    get first fibonacci number of given length
    problem25
    '''
    if type(digits) != int:
        raise TypeError

    a,b = 0, 1
    length = 1
    i = 0
    while len(str(a)) < digits:
        i = i + 1
        a , b = b, a+b
    return i
