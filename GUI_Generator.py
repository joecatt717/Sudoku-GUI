from random import shuffle
import copy
import pygame
import time
pygame.font.init()

"""
Sudoku Generator

input: grid can be a 2-D matrix of a Sudoku puzzle to solve, or None to generate a new puzzle.
"""


class SudokuGenerator:
    """generates and solves Sudoku puzzles using a backtracking algorithm"""
    def __init__(self, grid=None, difficulty=3):
        self.counter = 0
        #path is for the matplot lib animation
        self.path = []
        #if a grid/puzzle is pass in, make a copy and solve it
        self.difficulty = difficulty
        if grid:
            if len(grid[0]) == 9 and len(grid) == 9:
                self.grid = grid
                self.original = copy.deepcopy(grid)
                self.solve_input_sudoku()
            else:
                print("input needs to be a 9x9 matrix")
        else:
            #if no puzzle is passed, generate one
            self.grid = [[0 for i in range(9)] for j in range(9)]
            self.generate_puzzle()
            self.original = copy.deepcopy(self.grid)



    def solve_input_sudoku(self):
        '''solves a puzzle'''
        self.generate_solution(self.grid)
        return


    def generate_puzzle(self):
        '''generates a new puzzle and solves it'''
        self.generate_solution(self.grid)
        self.print_grid('Full Solution')
        self.remove_numbers_from_grid()
        self.print_grid('With removed numbers')
        return


    def print_grid(self, grid_name=None):
        if grid_name:
            print(grid_name)
        row = 0
        col = 0
        for i in self.grid:
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


    def test_sudoku(self, grid):
        '''tests each square to make sure it is a valid puzzle'''
        for row in range(9):
            for col in range(9):
                num = grid[row][col]
                #remove number from grid to test if it's valid
                grid[row][col] = 0
                if not self.valid_location(grid,row,col,num):
                    return False
                else:
                    #put num back in grid
                    grid[row][col] = num
        return True

    def num_used_in_row(self, grid, row, number):
        '''returns True if the number has been used in that row'''
        if number in grid[row]:
            return True
        return False


    def num_used_in_column(self, grid, col, number):
        '''returns True if the number has been used in that col'''
        for i in range(9):
            if grid[i][col] == number:
                return True
        return False


    def num_used_in_subgrid(self, grid, row, col, number):
        sub_row = (row // 3) * 3
        sub_col = (col // 3) * 3
        for i in range(sub_row, (sub_row +3)):
            for j in range(sub_col, (sub_col +3)):
                if grid[i][j] == number:
                    return True
        return False

    
    def valid_location(self, grid, row, col, number):
        '''return False if the number has been used in the row, column or subgrid'''
        if self.num_used_in_row(grid,row,number):
            return False
        elif self.num_used_in_column(grid,col,number):
            return False
        elif self.num_used_in_subgrid(grid, row, col, number):
            return False
        return True


    def find_empty_square(self,grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return (i,j)
        return


    def solve_puzzle(self, grid):
        '''solve the sudoku puzzle with backtracking'''
        for i in range(0,81):
            row = i // 9
            col = i % 9
            #find next empty cell
            if grid[row][col] == 0:
                for number in range(1,10):
                    #check that the number hasn't been used in row/col/subgrid
                    if self.valid_location(grid,row,col,number):
                        grid[row][col] = number
                        if not self.find_empty_square(grid):
                            self.counter += 1
                            break
                        else:
                            if self.solve_puzzle(grid):
                                return True
                break
        grid[row][col] = 0
        return False


    def generate_solution(self, grid):
        '''generates a full solution with backtracking'''
        number_list = [1,2,3,4,5,6,7,8,9]
        for i in range(0,81):
            row = i//9
            col = i%9
            #find next empty cell
            if grid[row][col] == 0:
                shuffle(number_list)
                for number in number_list:
                    if self.valid_location(grid,row,col,number):
                        self.path.append((number,row,col))
                        grid[row][col] = number
                        if not self.find_empty_square(grid):
                            return True
                        else:
                            if self.generate_solution(grid):
                                #if the grid is full
                                return True
                break
        grid[row][col] = 0
        return False
        

    def get_non_empty_squares(self,grid):
        '''return a shuffled list of non-empty squares'''
        non_empty_squares = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] != 0:
                    non_empty_squares.append((i,j))
        shuffle(non_empty_squares)
        return non_empty_squares
        

    def remove_numbers_from_grid(self):
        '''remove numbers from the grid to creat the puzzle'''
        #get all non-empty squares from the grid
        non_empty_squares = self.get_non_empty_squares(self.grid)
        non_empty_squares_count = len(non_empty_squares)
        #could change this to increase / decrease difficulty
        #gives the computer chances to find numbers that would be valid to remove
        rounds = self.difficulty
        while rounds > 0 and non_empty_squares_count >=17:
            #there should be at least 17 clues
            #pop off a random filled square, and take it to zero
            row,col = non_empty_squares.pop()
            non_empty_squares_count -= 1
            #might need to put the square value back if there is more than one solution
            removed_square = self.grid[row][col]
            self.grid[row][col] = 0
            #make a copy of the grid to solve
            grid_copy = copy.deepcopy(self.grid)
            #initialize solutions counter to zero
            self.counter = 0
            self.solve_puzzle(grid_copy)
            #if there is more than one solution, put the last removed cell back into the grid
            if self.counter != 1:
                self.grid[row][col] = removed_square
                non_empty_squares_count += 1
                rounds -= 1
        return

## altering the second input value changes the difficulty
grid = SudokuGenerator()
grid.print_grid


class Grid(SudokuGenerator):

    board = SudokuGenerator().grid

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def place(self, val):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            self.update_model()

            if self.valid_location(self.model, row, col, val) and self.solve_puzzle(self.model):
                return True
            else:
                self.cubes[row][col].set(0)
                self.cubes[row][col].set_temp(0)
                self.update_model()
                return False

    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    def draw(self, win):
        # Draw grid lines
        gap = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, (0,0,0), (i*gap, 0), (i*gap, self.height), thick)
            # Draw Cubes
            for i in range(self.rows):
                for j in range(self.cols):
                    self.cubes[i][j].draw(win)

    def select(self, row, col):
        #reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

    def click(self, pos):
        """
        :param: pos
        :return: (row, col)
        """
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y), int(x))
        else:
            return None

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128,128,128))
            win.blit(text, (x+5, y+5))
        elif not(self.value == 0):
            text = fnt.render(str(self.value), 1, (0,0,0))
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(win, (255,0,0), (x,y, gap, gap), 3)

    def set(self, val):
        self.value = val

    def set_temp(self, val):
        self.temp = val


def redraw_window(win, board, time, strikes):
    win.fill((255,255,255))
    # Draw (time)
    fnt = pygame.font.SysFont("comicsans", 40)
    text = fnt.render("Time: " + format_time(time), 1, (0,0,0,))
    win.blit(text, (540 - 160, 560))
    # Draw (strikes)
    text = fnt.render("X " * strikes, 1, (255,0,0))
    win.blit(text, (20, 560))
    # Draw (grid and board)
    board.draw(win)

def format_time(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat

def main():
    win = pygame.display.set_mode((540,600))
    pygame.display.set_caption("Sudoku")
    board = Grid(9,9,540,540)
    key = None
    run = True
    start = time.time()
    strikes = 0
    while run:

        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp !=0:
                        if board.place(board.cubes[i][j].temp):
                            print("Success!")
                        else:
                            print("Wrong!")
                            strikes += 1
                        key = None

                        if board.is_finished():
                            print("Game over")
                            run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            board.sketch(key)
        
        redraw_window(win, board, play_time, strikes)
        pygame.display.update()


main()
pygame.quit()