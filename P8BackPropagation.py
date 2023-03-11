import numpy as np

def solve_sudoku(puzzle):
    """
    Solves a Sudoku puzzle using backtracking algorithm.

    Args:
    puzzle: 9x9 numpy array representing the puzzle to be solved. 
            Empty cells are represented by 0.

    Returns:
    solution: 9x9 numpy array representing the solved puzzle.
              Returns None if there is no solution.
    """

    def is_valid(row, col, num):
        """
        Returns True if the given number is a valid choice for the given
        cell in the puzzle.

        Args:
        row: int representing row index of the cell
        col: int representing column index of the cell
        num: int representing number to be checked

        Returns:
        bool: True if the given number is a valid choice for the given cell
              in the puzzle.
        """
        # Check row and column
        for i in range(9):
            if puzzle[row][i] == num or puzzle[i][col] == num:
                return False
        
        # Check 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if puzzle[box_row+i][box_col+j] == num:
                    return False
        return True

    def solve():
        """
        Recursive function to solve the puzzle.

        Returns:
        bool: True if puzzle is solved, False if no solution found.
        """
        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(row, col, num):
                            puzzle[row][col] = num
                            if solve():
                                return True
                            puzzle[row][col] = 0
                    return False
        return True
    
    # Call the recursive solve function
    if solve():
        return puzzle
    else:
        return None

# Example usage

# Define input Sudoku puzzle
input_puzzle = np.array([
    [0, 0, 0, 0, 0, 3, 0, 2, 0],
    [0, 8, 0, 0, 0, 7, 0, 0, 9],
    [6, 0, 2, 0, 0, 0, 5, 0, 0],
    [7, 0, 0, 0, 0, 0, 6, 0, 0],
    [0, 0, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 0, 7, 0],
    [0, 0, 0, 0, 0, 0, 7, 8, 3],
    [0, 0, 0, 3, 4, 0, 0, 0, 6],
    [0, 0, 0, 2, 0, 0, 0, 0, 0]
])
solution = solve_sudoku(input_puzzle)
if solution is None:
    print("No solution found.")
else:
    print('solution')
    print(solution)

