grid = []

grid.append([0,0,4,0,7,0,3,0,0])
grid.append([7,0,0,0,6,0,0,8,0])
grid.append([9,0,0,0,5,3,0,7,1])
grid.append([0,0,3,0,0,0,0,2,0])
grid.append([2,0,0,0,3,0,7,9,4])
grid.append([0,0,7,6,1,0,0,0,8])
grid.append([0,0,1,9,0,6,0,5,0])
grid.append([8,0,0,0,0,0,0,0,7])
grid.append([0,0,0,0,8,0,0,1,0])

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
    find = find_empty(grid)
    if not find:
        return True
    else:
        row, col = find ## sets the variables row and col to the closests 0 value  (y, x) in the grid

    for i in range(1,10): ## finding the value from 1 to 10 for the given cell
        if valid(grid, i, (row, col)):
            grid[row][col] = i

            if solve(grid):
                return True
            
            grid[row][col] = 0

    return False

print_grid(grid)
solve(grid)
print("\n")
print_grid(grid)