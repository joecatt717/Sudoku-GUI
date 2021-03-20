from random import shuffle

grid = [[0 for i in range(9)] for j in range(9)]


class Grid:

    def __init__(self):
        self.grid = grid

    def generate_solution(self, grid):
        #generates a full solution with backtracking
        number_list = [1,2,3,4,5,6,7,8,9]
        for i in range(0,81):
            row=i//9
            col=i%9
            #find next empty cell
            if grid[row][col]==0:
                shuffle(number_list)      
                for number in number_list:
                    if self.valid_location(grid,row,col,number):
                        self.path.append((number,row,col))
                        grid[row][col]=number
                        if not self.find_empty_square(grid):
                            return True
                        else:
                            if self.generate_solution(grid):
                                #if the grid is full
                                return True
                break
        grid[row][col]=0  
        return False

def remove_numbers_from_grid(self):
    """remove numbers from the grid to create the puzzle"""
    #get all non-empty squares from the grid
    non_empty_squares = self.get_non_empty_squares(self.grid)
    non_empty_squares_count = len(non_empty_squares)
    rounds = 3
    while rounds > 0 and non_empty_squares_count >= 17:
        #there should be at least 17 clues
        row,col = non_empty_squares.pop()
        non_empty_squares_count -= 1
        #might need to put the square value back if there is more than one solution
        removed_square = self.grid[row][col]
        self.grid[row][col]=0
        #make a copy of the grid to solve
        grid_copy = copy.deepcopy(self.grid)
        #initialize solutions counter to zero
        self.counter=0      
        self.solve_puzzle(grid_copy)   
        #if there is more than one solution, put the last removed cell back into the grid
        if self.counter!=1:
            self.grid[row][col]=removed_square
            non_empty_squares_count += 1
            rounds -=1
    return

new_grid = Grid()
new_grid.generate_solution(grid)