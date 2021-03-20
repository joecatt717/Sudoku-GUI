import random
from random import shuffle
from random import randint

def blank_grid():
    grid = []
    grid.append([0,0,0,0,0,0,0,0,0])
    grid.append([0,0,0,0,0,0,0,0,0])
    grid.append([0,0,0,0,0,0,0,0,0])
    grid.append([0,0,0,0,0,0,0,0,0])
    grid.append([0,0,0,0,0,0,0,0,0])
    grid.append([0,0,0,0,0,0,0,0,0])
    grid.append([0,0,0,0,0,0,0,0,0])
    grid.append([0,0,0,0,0,0,0,0,0])
    grid.append([0,0,0,0,0,0,0,0,0])
    return grid


def print_grid(grid):
    row = 0
    col = 0
    for i in grid:
        if row % 3 == 0 and row != 0:
            print("---------------------")
        row += 1

        for j in i:
            print((j), end= " ")
            col += 1
            if col % 3 == 0 and col != 0 and col != 9:
                print("|", end= " ")
            elif col == 9:
                print('')
                col = 0


def valid(grid, value, pos):
## grid = the the grid input from above
## value = the value in the given cell
## pos = y value from 0 to 8 , x value from 0 to 8
## (row) = pos[0]
## (col) = pos[1]
## check row
    for i in range(9):
        if grid[pos[0]][i] == value and pos[1] != i:
            return False

## check col
    for i in range(9):
        if grid[i][pos[1]] == value and pos[0] !=i:
            return False

## check boxes
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if grid[i][j] == value and (i,j) != pos:
                return False

    return True


def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j ##given as position y, x

    return None


def solve(grid):
    solved_grid = grid
    find = find_empty(solved_grid)
    if not find:
        return True
    else:
        row, col = find ## sets the variables row and col to the closests 0 value  (y, x) in the grid

    for i in range(1,10): ## finding the value from 1 to 9 for the given cell
        if valid(solved_grid, i, (row, col)):
            solved_grid[row][col] = i

            if solve(solved_grid):
                return True
            
            solved_grid[row][col] = 0

    return False


def solve_back(grid):
    find = find_empty(grid)
    if not find:
        return True
    else:
        row, col = find ## sets the variables row and col to the closests 0 value  (y, x) in the grid

    for i in range(9,0,-1): ## finding the value from 1 to 9 for the given cell
        if valid(grid, i, (row, col)):
            grid[row][col] = i

            if solve(grid):
                return True
            
            grid[row][col] = 0

    return False


def grid_fill(grid):

    base_row = [1,2,3,4,5,6,7,8,9]
    shuffle(base_row)

    for i in range(9):
        grid[0][i] = base_row[i]


    return grid
'''
def make_puzzle(grid):
## randomly remove numbers until only one possible solution remains
    new_grid = grid
    y = randint(0,8)
    x = randint(0,8)
    new_grid[y][x] = 0

    solved_forward = new_grid
    solved_backward = new_grid

    solve(solved_forward)
    solve_back(solved_backward)

    grid = new_grid

    if solved_forward != solved_backward:
        return grid
    else:
        make_puzzle(grid)


    while solved_forward == solved_backward:
        y = randint(0,8)
        x = randint(0,8)
        new_grid[y][x] = 0

        solved_forward = new_grid
        solved_backward = new_grid

        solve(solved_forward)
        solve_back(solved_backward)    
    else:
        return(grid)
    '''


grid = blank_grid()
print_grid(grid)

solved_forward = grid
solved_backward = grid


def make_puzzle(empty_grid):
    grid = empty_grid

    val = randint(1,9)
    row = randint(0,8)
    col = randint(0,8)

    while not valid(grid, val, (row, col)):
        val = randint(1,9)
        row = randint(0,8)
        col = randint(0,8)
    else:
        grid[row][col] = val

    solved_forward = grid
    solved_backward = grid

    solve(solved_forward)
    solve_back(solved_backward)

    while solved_forward != solved_backward:
        make_puzzle(grid)
    else:
        return grid

puzzle = make_puzzle(blank_grid())


print('\n')
print_grid(puzzle)


    ## find random coordinate

    ## fill coordinate with random number (that works...)

    ## solve that board both ways

    ## check if the solutions match

    ## repeat

'''
print("\n")
base_grid = (grid_fill(grid))
print_grid(base_grid)

print("\n")
tobe_solved = base_grid
solve(tobe_solved)
solved_grid = tobe_solved
print_grid(solved_grid)

print("\n")
puzzle = solved_grid

print("\n")
puzzle = make_puzzle(solved_grid)
print_grid(puzzle)

puzzle = solved_grid
make_puzzle(puzzle)
print_grid(puzzle)

print("\n")
tobe_solved_back = puzzle
solve_back(tobe_solved_back)
solved_back = tobe_solved_back
print_grid(solved_back)

print(solve_back == solved_grid)

#Start Removing Numbers one by one

#A higher number of attempts will end up removing more numbers from the grid
#Potentially resulting in more difficiult grids to solve!
attempts = 5 
counter=1
while attempts>0:
    #Select a random cell that is not already empty
    row = randint(0,8)
    col = randint(0,8)
    while puzzle[row][col]==0:
        row = randint(0,8)
        col = randint(0,8)
    #Remember its cell value in case we need to put it back  
    backup = puzzle[row][col]
    puzzle[row][col]=0
  
    #Take a full copy of the grid
    copyGrid = []
    for r in range(0,9):
        copyGrid.append([])
        for c in range(0,9):
            copyGrid[r].append(puzzle[r][c])
  
    #Count the number of solutions that this grid has (using a backtracking approach implemented in the solveGrid() function)
    counter=0      
    solve(copyGrid)   
    #If the number of solution is different from 1 then we need to cancel the change by putting the value we took away back in the grid
    if counter!=1:
        puzzle[row][col]=backup
        #We could stop here, but we can also have another attempt with a different cell just to try to remove more numbers
        attempts -= 1

print_grid(puzzle)
'''