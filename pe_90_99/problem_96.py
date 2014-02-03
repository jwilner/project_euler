def make_grids(path):
    '''
      process data into SudokuSolver form
      '''
        sudokus = []
        with open(path) as csvfile:
            sudoku_grids = csv.reader(csvfile)
            while True:
                try:
                    next(sudoku_grids)
                    sudokus.append([i for i in itertools.islice(sudoku_grids,9)])
                except StopIteration:
                    break
        new_sudokus = []
        for s in sudokus:
            new_s = {}
            for x,row in enumerate(s):
                for y,val in enumerate(row[0]):
                    new_s[(x,y)] = {int(val)}
            new_sudokus.append(new_s)
        return new_sudokus

def test_all(sudoku_grids,catch_fire = False):
    successes,failures = {},{}
    for i,grid in enumerate(sudoku_grids):
        solver = SudokuSolver(grid)
        result = solver.solve()
        for cells in solver._get_groups(): #whoops, used a private method
            values = [result[cell] for cell in cells]
            joined_sets = list(itertools.chain(*values))
            if len(joined_sets) != 9 or 0 in joined_sets:
                if not catch_fire:
                    failures[i] = result
                    break
                else:
                    raise ValueError('Problem found in grid '+str(i)+': '+''.join(str(j) for j in joined_sets))
        else:
            successes[i] = result
    return successes,failures

def pretty_print(grid):
    '''
    ancillary function
    '''
    for x in range(0,9):
        row = ''
        for y in range(0,9):
            current = grid[x,y]
            if len(current) > 1 or current == {0}:
                row += '{ } ';
            else:
                row += str(grid[(x,y)])+' '
        print row

class SudokuSolver():
    def __init__(self,input_grid):
        '''
        grids are dictionaries with tuple keys holding the coordinates
        '''
        self._input_grid = input_grid
        self._output_grid = {(x,y):{d for d in range(1,10)} for x in range(0,9) for y in range(0,9)} #grid where each cell has the set of all 9 possible numbers
        self._incomplete = set(self._output_grid.keys()) #tracks all remaining 'incomplete cells' -- cells with more than one value

    def solve(self):
        '''
        main interface
        '''
        for (x,y),value in self._input_grid.items(): #this is the only time 'input grid' is needed -- afterwards, all data internalized
            if value != {0}: #input_grid uses {0} to mark blank cell
                self._set_cell_value((x,y),value)

        for group in self._get_groups():
            self._check_for_unique(group)

        return self._output_grid

    def _set_cell_value(self,cell,value):
        '''
        essentially a wrapper on standard assignment: once we've reduced a cell to one value
        via this func, we need to remove that value from all dependent cells
        '''
        self._output_grid[cell] = value
        self._distribute(cell)

    def _distribute(self,cell):
        '''
        this function is only called after the value or possible values for a cell have been changed.
        If there is only one value, then we know it doesn't occur in any dependents.

        If multiple values, then check for this logic: if {1,2},{1,2},{1,2,3}, then {1,2},{1,2},{3}.
        Expressed more generally, if the set A ({1,2}) occurs in a group of sets B as many times as A has members,
        then any other sets in B which have A as a subset can have the members of A removed. If you didn't,
        there wouldn't be enough remaining numbers to go around.
        '''
        values = self._output_grid[cell]
        length = len(values)
        if length == 1:
            self._incomplete.discard(cell) #remove from incomplete now and not at 'set cell value' because this function is ALWAYS called when changing value
            for d in self._dependents(cell):
                self._diff(d,cell)
        else:
            for group in (set(g(cell)) for g in (self._row,self._col,self._box)): #look at each group of dependents as a whole (as opposed to _dependents func)
                if length == 1+sum(1 for other in group if values == self._output_grid[other]): #if A occurs in B as many times as A has members...
                    for target in group:
                        if self._output_grid[target] != values:
                            self._diff(target,cell)

    def _diff(self,target,cell):
        '''
        Compare target and cell and remove any values in cell from target ,(e.g. diff({1,2,3,4},{3,4})
        = {1,2},{3,4}). This function doesn't itself assure that it's making a valid sudoku operation.
        '''
        if self._output_grid[target].intersection(self._output_grid[cell]): #why is this test here again?
            self._output_grid[target].difference_update(self._output_grid[cell]) #remove the intersection
            self._distribute(target) #changed values, so call distribute

    def _check_for_unique(self,group):
        '''
        If a number only occurs once in a whole group then the cell where it occurs must have it as the cell's
        value (e.g. {3,1,2},{2,3,4},{4,3,5,2} then {1},{2,3,4},{4,3,5,2}).
        '''
        for d in range(1,10):
            cells_with_d = [cell for cell in group if d in self._output_grid[cell]]
            if len(cells_with_d) == 1:
                (cell_with_d,) = cells_with_d #tuple unpack list
                if len(self._output_grid[cell_with_d]) != 1:
                    self._set_cell_value(cell_with_d,{d})

    def _dependents(self,cell):
        '''
        this function returns each dependent cell individually
        '''
        return itertools.chain(self._row(cell),self._col(cell),self._box(cell))

    def _row(self,cell):
        return ((d,cell[1]) for d in range(0,9) if d != cell[0])

    def _col(self,cell):
        return ((cell[0],d) for d in range(0,9) if d != cell[1])

    def _box(self,cell):
        box_x,box_y = (cell[0]//3)*3,(cell[1]//3)*3
        return  ((a,b) for a in range(box_x,box_x+3) for b in range(box_y,box_y+3) if (a,b) != cell)

    def _get_groups(self):
        reps = ((0,0),(3,1),(6,2),(1,3),(4,4),(7,5),(2,6),(5,7),(8,8)) #each of these cells has a unique column, row, and box
        for method in (self._row,self._col,self._box):
            for cell in reps:
                yield {c for c in method(cell)}|{cell}


if __name__ == '__main__':
    grids = make_grids('sudoku.txt')
    successes,failures = test_all(grids)
    print len(successes),'successes and',len(failures),'failures'
    for gridNo,failure in failures.items():
        print 'Failed on grid',gridNo,': '
        pretty_print(failure)
