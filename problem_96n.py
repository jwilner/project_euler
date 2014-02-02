import sys
from itertools import islice


def get_sudokus(filename):
    with open(filename, 'r') as f:
        lines = ([int(c) for c in l] for l in
                 (l for l in (l.strip('\n') for l in f) if l.isdigit()))
        while True:
            grid = list(islice(lines, 9))
            if not grid:
                break
            yield [((x, y), v) for y, row in enumerate(grid)
                   for x, v in enumerate(row) if v]


def solve_sudoku(cell_values):
    ''' initial list of tuple of coords and value for coords having value 1-9
    --> list of coords and values representing completed sudoku'''

    grid = {(x, y): set(xrange(1, 10)) for x in xrange(9) for y in xrange(9)}
    grids = [grid]

    box_top_left = lambda c: (c // 3) * 3
    find_incomplete = lambda: {k for k, v in grid.iteritems() if len(v) > 1}

    incomplete = find_incomplete()

    def get_row((x, y)):
        return ((new_x, y) for new_x in xrange(9) if new_x != x)

    def get_column((x, y)):
        return ((x, new_y) for new_y in xrange(9) if new_y != y)

    def get_box((x, y)):
        top_x, top_y = box_top_left(x), box_top_left(y)
        x_diff, y_diff = x - top_x, y - top_y
        return ((top_x + x_offset, top_y + y_offset)
                for x_offset in xrange(3) for y_offset in xrange(3)
                if x_offset != x_diff and y_offset != y_diff)

    getters = get_row, get_column, get_box

    def get_every_group():
        for x in xrange(9):
            yield get_column((x, 0))
        for y in xrange(9):
            yield get_row((0, y))
        for top_left in zip((box_top_left(x) for x in xrange(9)),
                            [0, 3, 6] * 3):
            yield get_box(top_left)

    def get_neighbors(position):
        seen = set()
        for pos in (getter(position) for getter in getters):
            for p in pos:
                if p not in seen:
                    yield p
                    seen.add(p)

    # sudoku strategies

    def handle_duplicates(position):
        '''{1,2}, {1,2}, {1,2,3,4}, {1,2,4,5}, {3,5} -->
           {1,2}, {1,2}, {3,4},     {4,5},     {3,5}'''
        values = grid[position]
        num_to_check = len(values) - 1  # i.e. discounting values at position
        for neighbor_group in (set(getter(position)) for getter in getters):
            dopplegangers = {neighbor for neighbor in neighbor_group
                             if values == grid[neighbor]}
            if len(dopplegangers) == num_to_check:
                for different in neighbor_group - dopplegangers:
                    set_cell_value(different, grid[different] - values)

    def remove_from_neighbors(position):
        '''{3}, {1, 2, 3}, {1, 2} -->
           {3}, {1, 2},    {1, 2}'''
        values = grid[position]
        for neighbor in get_neighbors(position):
            set_cell_value(neighbor, grid[neighbor] - values)

    def handle_unique(group, value):
        '''{1,2,3}, {1,2,3}, {1,2,3,4}, {2,3} -->
           {1,2,3}, {1,2,3}, {4},       {2,3}'''
        cells_with_value = {cell for cell in group if value in grid[cell]}
        try:
            (only_cell_with_value,) = cells_with_value
            set_cell_value(only_cell_with_value, {value})
        except ValueError:  # then not just one cell, so do nothing
            pass

    def address_any_uniques():
        for group in get_every_group():
            for d in xrange(9):
                handle_unique(group, d)

    #  control flow function

    def set_cell_value(position, values):
        '''Groups (recursive) operations to be called anytime cell value
        changes'''
        old_values = grid[position]
        if old_values != values:  # if values have changed, then update stuff
            grid[position] = values
            num_values = len(values)
            if num_values == 1:
                incomplete.discard(position)
                remove_from_neighbors(position)
            else:
                handle_duplicates(position)

    # operations for final exhaustive approach if necessary

    def is_group_correct(group):
        ''' I.e. all values 1-9 are present (correct != complete)'''
        values = set()
        for val in (grid[pos] for pos in group):
            values |= val
        return len(values) == 9

    def is_grid_correct():
        return all(is_group_correct(group) for group in get_every_group())

    def make_grid_copy():
        return {k: s.copy() for k, s in grid.items()}

    def make_assumption():
        '''Finds the incomplete cell with the fewest options (e.g. 2, which
        likely), and returns a tuple of the cell and one of those options'''
        most_likely = min(incomplete, key=lambda x: len(grid[x]))
        assumed_val = grid[most_likely].pop()  # prob right:  1 / len(vals)
        return most_likely, assumed_val

    # deterministic procedure

    for position, value in cell_values:  # processing input values
        set_cell_value(position, {value})

    address_any_uniques()

    while incomplete:  # then begin exhaustive approach on leftovers
        if not is_grid_correct():
            grids.pop()
            try:
                grid = grids[-1]
            except IndexError:
                print "We've done fucked up."
                sys.exit(1)
            incomplete = find_incomplete()

        grid = make_grid_copy()
        grids.append(grid)

        cell, assumed_val = make_assumption()
        set_cell_value(cell, {assumed_val})
        address_any_uniques()

        if not is_grid_correct():  # roll back, reductio ad absurdum
            grids.pop()
            grid = grids[-1]
            incomplete = find_incomplete()
            # remove assumed value from options
            set_cell_value(cell, grid[cell] - {assumed_val})

    return sorted((k, s.pop()) for k, s in grid.items())


def print_sudoku(sudoku):
    grid = dict(sudoku)
    row_string = " {} |" * 9
    horizontal = "----" * 9
    print horizontal
    for y in xrange(9):
        row = []
        for x in xrange(9):
            row.append(grid[x, y] if (x, y) in grid else 'X')
        print row_string.format(*row)
        print horizontal


if __name__ == '__main__':
    sudokus = get_sudokus('problem_96.txt')
    for i, sudoku in enumerate(sudokus):
        print "Sudoku # {}".format(i + 1)
        print "Input: "
        print_sudoku(sudoku)
        result = solve_sudoku(sudoku)
        print "Output: "
        print_sudoku(result)
