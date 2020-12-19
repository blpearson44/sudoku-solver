import numpy as np

puzzle = []


def create_puzzle(puzzle_string):
    """Creates the puzzle from an inserted string which is 81 digits long (0 for
    blanks)"""
    global puzzle
    if len(puzzle_string) == 81:
        for i in range(0, len(puzzle_string), 9):
            row = puzzle_string[i:i+9]
            temp = []
            for num in row:
                temp.append(int(num))
            puzzle.append(temp)
        print("The Puzzle:")
        print(np.matrix(puzzle))
    else:
        print("The puzzle key must have 81 digits.")


def possible(row, col, digit):
    """Determines if the placement is possible

    Args:
        row (int): Index for the row 
        col (int): Index for the column
        digit (int): Number to be placed at location

    Returns:
        bool: True if placement is possible, False otherwise
    """
    global puzzle
    for i in range(9):
        if(puzzle[row][i]) == digit:
            return False
    for i in range(9):
        if(puzzle[i][col]) == digit:
            return False
    # finds the boxes, could likely be implemented using modulo as well
    row_square = (row//3)*3
    col_square = (col//3)*3
    for i in range(3):
        for j in range(3):
            if puzzle[row_square + i][col_square+j] == digit:
                return False
    return True


num_solutions = 0
show_solutions = True


def solve():
    """Solves the sudoku puzzle through backgtracking"""
    global puzzle
    global num_solutions
    global show_solutions
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                for digit in range(1, 10):
                    if possible(row, col, digit):
                        puzzle[row][col] = digit
                        # solve recursively until failure or until a solution is
                        # found
                        solve()
                        # backtrack
                        puzzle[row][col] = 0
                return
    num_solutions += 1
    if show_solutions:
        print("Solution {}:".format(num_solutions))
        print(np.matrix(puzzle))
        response = str(input("More?\n"))
        show_solutions = (response != "n")


puzzle_key = str(input("Puzzle String:\n"))
create_puzzle(puzzle_key)

print("Input N to skip showing solutions.")
solve()
print("That puzzle had {} solution(s).".format(num_solutions))
