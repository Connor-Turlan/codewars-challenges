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



def _filter_sudoku(puzzle, filter):
    changed = False;
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] != 0: continue
            
            for i in range(1, 10):
                if isSafe(puzzle, row, col, i):
                    filter[row][col].append(i)
            
            if len(filter[row][col]) == 1:
                changed = True
                puzzle[row][col] = filter[row][col][0]
                filter[row][col] = []
    
    return changed, filter

def filter_sudoku(PUZZLE):
    FILTER = [[[] for i in range(9)] for j in range(9)]
    changed, filter = _filter_sudoku(PUZZLE, FILTER)
    while changed:
        FILTER = [[[] for i in range(9)] for j in range(9)]
        changed, filter = _filter_sudoku(PUZZLE, FILTER)
    
    return FILTER

def solve_sudoku(puzzle, filter):
    # get the next free cell.
    row, col = getUnassignedLocation(puzzle)

    # if the cell is 9,9 the sudoku is solved.
    if (row == 9 and col == 9): return True

    # try insert 1 thru 9.
    for i in filter[row][col]:
        if isSafe(puzzle, row, col, i):
            puzzle[row][col] = i
            if solve_sudoku(puzzle, filter): return True

    # if we can't insert a number, the current solve is wrong. reset the cell.
    puzzle[row][col] = 0
    return False



def validate(puzzle):
    if len(puzzle) != 9: return False
    if False in [len(row) == 9 for row in puzzle]: return False
    
    if max([row.count(i) for row in puzzle for i in range(1, 10)]) > 1: return False
    if max([getPuzzleCol(puzzle, col).count(i) for col in range(9) for i in range(1, 10)]) > 1: return False
    if max([getPuzzleBox(puzzle, box % 3, box // 3).count(i) for box in range(9) for i in range(1, 10)]) > 1: return False

    return True



def sudoku_solver(PUZZLE):
    # validate the puzzle
    if not validate(PUZZLE): return PUZZLE

    FILTER = filter_sudoku(PUZZLE)
    solved = solve_sudoku(PUZZLE, FILTER)
    return PUZZLE


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
        [1, 4, 0, 2, 0, 1, 0, 6, 0],
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

    print("Puzzle")
    [print(row) for row in PUZZLE]
    sudoku_solver(PUZZLE)
    [print(row) for row in PUZZLE]