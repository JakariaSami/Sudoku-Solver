# Initial Sudoku board
board = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]


# Function to solve the Sudoku puzzle recursively
def solve(gameboard):
    # Find the next blank spot
    inputField = blank_spots(gameboard)

    # If there are no more blank spots, the Sudoku is solved
    if not inputField:
        return True
    else:
        row, col = inputField

    # Try filling in numbers from 1 to 9
    for i in range(1, 10):
        if isSolvable(gameboard, i, (row, col)):
            gameboard[row][col] = i

            # Recursively try to solve the Sudoku
            if solve(gameboard):
                return True

            # Backtrack if the current configuration is not valid
            gameboard[row][col] = 0

    # If no number from 1 to 9 works, backtrack
    return False


# Function to check if a number can be placed in a certain position
def isSolvable(gameboard, inputNum, coord):
    # Check row
    for i in range(9):
        if gameboard[coord[0]][i] == inputNum and coord[1] != i:
            return False

    # Check column
    for i in range(9):
        if gameboard[i][coord[1]] == inputNum and coord[0] != i:
            return False

    # Check box
    box_x = coord[1] // 3
    box_y = coord[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if gameboard[i][j] == inputNum and (i, j) != coord:
                return False

    return True


# Function to display the Sudoku board
def display(gameboard):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("------------------------")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(gameboard[i][j])
            else:
                print(str(gameboard[i][j]) + " ", end="")


# Function to find the next blank spot
def blank_spots(gameboard):
    for i in range(9):
        for j in range(9):
            if gameboard[i][j] == 0:
                return (i, j)

    return None


# Display initial board
print("\n \n Initial board: \n \n")
display(board)

# Solve the Sudoku puzzle
solve(board)

# Display solved version
print("\n \n Solved version: \n \n")
display(board)
