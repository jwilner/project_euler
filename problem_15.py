
def lattice_path(n):
    '''
    grid representing problem space
    problem15
    '''
    if type(n) != int:
        raise TypeError

    grid = []
    for i in range(1,n+2):
        grid.append([0]*(n+2))
    x = 0;

    while x < n+1:
        y = 0
        while y < n+1:
            ways = 0
            if x > 0:
                ways = ways + grid[x-1][y]
            if y > 0:
                ways = ways + grid[x][y-1]
            if ways == 0:
                ways = 1
                grid[x][y] = ways
            y = y + 1
        x = x + 1

    return grid
