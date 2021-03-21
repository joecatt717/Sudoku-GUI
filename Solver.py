'''
from puzzle_generator import get_puzzle
board = get_puzzle()
'''


#I = (verticle axis) length of the board is 9 nested lists
#"j" = (horizontal axis) each nested list has 9 parts

def print_board(board):
    # iterates through each row vertically 0 - 8
    for i in range(len(board)):
        #if the row is divisible by 3 except row 0 - creates a horizontal line
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        # iterates through each column horizontally, while iterating through i
        for j in range(len(board[0])):
            #if the column is divisible by 3 exept 0 - creates verical divider
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            #checks to see if the program has reached the end of a horizontal line
            # prints the value at the end, and allows it to enter a new row
            #otherwise, it ends each value with a " " instead.
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

                

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row (i) and the column (j)



#function to check if the board could yield a valid solution
#uses the current board, num = input number for the, position = [i][j] row and column
def valid(board, num, pos):
    #check if row is valid
    for x in range(len(board[0])):
        #check if each value in the row is equal to the input num, except for the value that we just input
        if board[pos[0]][x] == num and pos[1] != x:
            return False

    for y in range(len(board)):
        if board[y][pos[1]] == num and pos[0] != y:
            return False

    # check the 3x3 box if it is repeating a value
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x *3, box_x * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True



def solve(board):

    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

##---------------------------------------------------##

print_board(board)
solve(board)
print("-----------------------------------")
print_board(board)