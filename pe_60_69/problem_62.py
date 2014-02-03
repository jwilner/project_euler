from collections import defaultdict

def cube_permutations(n=5,start=3000):
    '''
    find the lowest cube the digits of which can be permuted to produce five other cubes
    problem 62
    '''
    cubes = defaultdict(list)
    while True:
        cube = start**3
        sig = ''.join(sorted(str(cube)))
        cubes[sig].append(cube)
        if len(cubes[sig]) >= n:
            return cubes[sig][0]
        start += 1

def n_power_n_digits():
    '''
    how many numbers are there with n digits that can be expressed as some number to the n
    problem62
    '''
    success = set()
    for i in range(1,10):
        j = 1
        powed = i**j
        digs = len(str(i**j))
        while j <= digs+1:
            if j == digs:
                success.add(powed)
            j += 1
            powed = i**j
            digs = len(str(i**j))
    return success
