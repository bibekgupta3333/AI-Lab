# Function to check if a queen can be placed on the board
def canPlaceQueen(board, row, col, N):
    # Check the current row for any queens
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal for any queens
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal for any queens
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # If the queen can be placed, return True
    return True

# Function to solve the n-queens problem using backtracking
def nQueenSolution(board, col, N):
    # If all queens are placed, return True
    if col >= N:
        return True

    # Iterate over all rows to check if a queen can be placed
    for i in range(N):
        if canPlaceQueen(board, i, col, N):
            # If a queen can be placed, update the board and move to the next column
            board[i][col] = 1

            # Recursively call the function to place the remaining queens
            if nQueenSolution(board, col + 1, N):
                return True

            # If the current placement does not result in a solution, backtrack and try the next row
            board[i][col] = 0

    # If no queen can be placed in this column, return False
    return False

# Get the chessboard size from the user
N = int(input("Chessboard size = "))

# Create a 2D array to represent the chessboard
printoutBoard = [[0] * N for i in range(N)]

# Call the nQueenSolution function to solve the problem
if nQueenSolution(printoutBoard, 0, N) == False:
    print("Solution failed")
else:
    # Print the final board configuration
    for i in range(N):
        for j in range(N):
            print(printoutBoard[i][j], end=" ")
        print("") 
