

def lattice_paths(n):
    """
    Returns the number of paths through a grid of size n by n
    """
    grid = {}

    def set_paths(a, b, paths_to_point):
        grid.update({(a, b): paths_to_point,
                     (b, a): paths_to_point})

    for v in xrange(n + 1):
        set_paths(v, 0, 1)

    for x in xrange(1, n + 1):
        for y in xrange(x, n + 1):
            set_paths(x, y, grid[x - 1, y] + grid[x, y - 1])

    return grid[n, n]


if __name__ == '__main__':
    print lattice_paths(20)
