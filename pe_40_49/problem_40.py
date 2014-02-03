
def champernowne_constant_position(n):
    '''
    returns nth fractional position of champernowne constant
    problem 40
    '''
    # total - positions - here - per - num value
    # 9             1-9             9      1     1-9
    # 189           10-189          180    2     10-99
    # 2889          190-2889        2700   3     100-999
    # 38889         2890-38889      36000  4         1000-9999

    #if someone asks for the nth position, find p
    p, range_start = 1,1
    while n - range_start >= 9*p*(10**(p-1)):
        range_start += 9*p*(10**(p-1))
        p += 1

    rel_position = n - range_start
    num_integer = rel_position // p
    num_digit = rel_position % p

    our_integer = 10**(p-1) + num_integer
    strung = str(our_integer)
    return int(strung[num_digit])
