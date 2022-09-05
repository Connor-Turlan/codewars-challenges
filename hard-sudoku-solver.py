""" class SudokuSolver():
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def used_in_row(self, row, num):
        for col in range(9):
            if self.get_puzzle_value(row, col) == num:
                return True
        return False

    def used_in_col(self, col, num):
        for row in range(9):
            if self.get_puzzle_value(row, col) == num:
                return True
        return False

    def used_in_box(self, x, y, num):
        for row in range(3):
            for col in range(3):
                if self.get_puzzle_value(x*3+col, y*3+row) == num:
                    return True
        return False

    def is_safe(self, row, col, num):
        urow = self.used_in_row(row, num)
        ucol = self.used_in_col(col, num)
        ubox = self.used_in_box(row//3, col//3, num)
        return not urow and not ucol and not ubox

    def get_unassigned_location(self):
        for i in range(9):
            for j in range(9):
                if self.get_puzzle_value(i, j) == 0:
                    return i, j
        return 9, 9

    def get_puzzle_value(self, row, col):
        return int(self.puzzle[row][col])

    def set_puzzle_value(self, row, col, value):
        self.puzzle[row][col]  = value

    def solve_sudoku(self):
        row, col = self.get_unassigned_location()

        if row == 9 and col == 9:
            return True

        for i in range(1, 10):
            if self.is_safe(row, col, i):
                self.set_puzzle_value(row, col, i)
                if self.solve_sudoku():
                    return True, self.puzzle

        self.set_puzzle_value(row, col, 0)
        return False, self.puzzle """

from re import L


def getRowAndColIndex(box, cell):
    return (
        (box // 3 * 27 + box % 3) +
        (cell // 3 * 9 + cell % 3)
    )

def getRow(box, cell):
    return getRowAndColIndex(box, cell) // 9

def getCol(box, cell):
    return getRowAndColIndex(box, cell) % 9



def getPuzzleRow(puzzle, row):
    return puzzle[row]

def getPuzzleCol(puzzle, col):
    return [row[col] for row in puzzle]

def getPuzzleBox(puzzle, x, y):
    return [puzzle[y*3+i][x*3+j] for i in range(3) for j in range(3)]


def usedInRow(puzzle, row, num):
    check = puzzle[row]
    return check.index(num) >= 0 if num in check else False

def usedInCol(puzzle, col, num):
    check = [row[col] for row in puzzle]
    return check.index(num) >= 0 if num in check else False

def usedInBox(puzzle, x, y, num):
    check = getPuzzleBox(puzzle, x, y)
    return check.index(num) >= 0 if num in check else False

def isSafe(puzzle, row, col, num):
    return (
        not usedInRow(puzzle, row, num) 
        and not usedInCol(puzzle, col, num) 
        and not usedInBox(puzzle, col // 3, row // 3, num)
    )



def getUnassignedLocation(puzzle):
    flat_puzzle = [i for row in puzzle for i in row]
    index = flat_puzzle.index(0) if 0 in flat_puzzle else -1
    return [index // 9, index % 9] if index >= 0 else [9, 9]



def solve_sudoku(puzzle):
    # get the next free cell.
    row, col = getUnassignedLocation(puzzle)

    # if the cell is 9,9 the sudoku is solved.
    if (row == 9 and col == 9): 
        return True

    # try insert 1 thru 9.
    for i in range(1, 10):
        if isSafe(puzzle, row, col, i):
            puzzle[row][col] = i
            if solve_sudoku(puzzle): 
                return True

    # if we can't insert a number, the current solve is wrong. reset the cell.
    puzzle[row][col] = 0
    return False



def sudoku_solver(puzzle):
	Solver = solve_sudoku(puzzle)
	solved = Solver.solve_sudoku()
	print(solved)
	return Solver.puzzle


def test(puzzle):
    print(puzzle)

    print('row')
    for i in range(9):
        print(getPuzzleRow(puzzle, i))
    
    print('col')
    for i in range(9):
        print(getPuzzleCol(puzzle, i))

    print('box')  
    for i in range(3):
        for j in range(3):
            print(getPuzzleBox(puzzle, j, i))


if __name__ == "__main__":
    print("Hello, World!")

    PUZZLE = [
            [0, 0, 6, 1, 0, 0, 0, 0, 8], 
            [0, 8, 0, 0, 9, 0, 0, 3, 0], 
            [2, 0, 0, 0, 0, 5, 4, 0, 0], 
            [4, 0, 0, 0, 0, 1, 8, 0, 0], 
            [0, 3, 0, 0, 7, 0, 0, 4, 0], 
            [0, 0, 7, 9, 0, 0, 0, 0, 3], 
            [0, 0, 8, 4, 0, 0, 0, 0, 6], 
            [0, 2, 0, 0, 5, 0, 0, 8, 0], 
            [1, 0, 0, 0, 0, 2, 5, 0, 0]
        ]

    PUZZLE = [
		[0, 4, 0, 2, 0, 1, 0, 6, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[9, 0, 5, 0, 0, 0, 3, 0, 7],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[5, 0, 7, 0, 8, 0, 1, 0, 4],
		[0, 1, 0, 0, 0, 0, 0, 9, 0],
		[0, 0, 1, 0, 0, 0, 6, 0, 0],
		[0, 0, 0, 7, 0, 5, 0, 0, 0],
		[6, 0, 8, 9, 0, 4, 5, 0, 3]
	]
    
    test(PUZZLE)

    status = solve_sudoku(PUZZLE)

    print('solved:', status)
    [print(row) for row in PUZZLE]