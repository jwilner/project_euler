import collections,random

def flea_circus(fleas):
    '''
    naive approach
    given 900 randomly jumping fleas originally distributed over a 30 by 30 grid, how many empty squares are expected to be left
    problem 213
    '''
    for i in range(0,50):
        for v,(x,y) in enumerate(fleas):
            options = []
            if x != 0: options.append((x-1,y))
            if y != 0: options.append((x,y-1))
            if x != 29: options.append((x+1,y))
            if y != 29: options.append((x,y+1))
            fleas[v] = random.choice(options)
    grid = set()
    for xy in fleas:
        grid.add(xy)
    return 900-len(grid)

def flea_position(coords,n = 50):
    '''
    Find the probability of all end points for a flea beginning at grid position x,y after n jumps
    problem 213
    '''
    x,y = coords
    matrix = collections.defaultdict(float)
    matrix[(x,y)] = 1
    for i in range(0,n):
        new_matrix = collections.defaultdict(float)
        for (x,y),v in matrix.items():
            options = []
            if x != 0: options.append((x-1,y))
            if y != 0: options.append((x,y-1))
            if x != 29: options.append((x+1,y))
            if y != 29: options.append((x,y+1))
            new_prob = v*(1/len(options))
            for (a,b) in options:
                new_matrix[(a,b)] += new_prob
        matrix = new_matrix
    return matrix

def full_matrix():
    '''
    Using resultant flea_positions, find the probability that any given square will be empty
    problem 213
    '''
    x,y = 30,30
    full_matrix = {(i,j):1 for i in range(0,x) for j in range (0,y)}
    for i in range(0,x):
        for j in range(0,y):
            result = flea_position((i,j))
            for (a,b),v in result.items():
                full_matrix[(a,b)] *= 1-v
    return full_matrix
