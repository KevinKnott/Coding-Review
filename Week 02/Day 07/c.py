# Sudoku Solver: https://leetcode.com/problems/sudoku-solver/
# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

#     Each of the digits 1-9 must occur exactly once in each row.
#     Each of the digits 1-9 must occur exactly once in each column.
#     Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

# The '.' character indicates empty cells.

# My initial couple of thoughts is that you could create a heap and get the highest freq of an element and to try and solve for it first
# Technically each row is actually a set so if you can find the only missing value from a given set you could solve that spot and add it
# to the horizontal and vertical set and the box set

# Honestly I have no clue how to program this but after looking at the solution it appears we could try brute forcing with bcktrack
# This means we try an option and dfs and if it fails we remove and try a different option continuing until completion


class Solution:
    def solveSudoku(self, board):

        def peekAdd(value, row, col):
            return not(value in rows[row] or value in cols[col] or value in boxs[box_index(row, col)])

        def addToSets(value, row, col):
            rows[row].add(value)
            cols[col].add(value)
            boxs[box_index(row, col)].add(value)
            board[row][col] = str(value)

        def removeFromSets(value, row, col):
            rows[row].remove(value)
            cols[col].remove(value)
            boxs[box_index(row, col)].remove(value)
            board[row][col] = '.'

        def getNextRowCol(row, col):
            # Check if we are at the end
            if col == N - 1 and row == N - 1:
                nonlocal solved
                solved = True
            else:
                # Increment col and if col overflows go to next row
                if col == N - 1:
                    backtrack(row+1)
                else:
                    backtrack(row, col+1)

        def backtrack(row=0, col=0):
            # if we have an empty space
            if board[row][col] == '.':
                # Loop through all possible values
                for value in range(1, 10):
                    # Check if we actually can place the value
                    if peekAdd(value, row, col):
                        # Add that value
                        addToSets(value, row, col)
                        # Go to next RC
                        getNextRowCol(row, col)
                        # check if we have solved everything
                        if not solved:
                            # if not we need to remove what was added
                            removeFromSets(value, row, col)

                            # if we have solved return it
            else:
                getNextRowCol(row, col)

        # Define box size to simulate 0->9 boxes of 3 x 3
        n = 3
        N = n * n

        # We have to figure out math for identifying box by row/col
        # Simple lambda function f(row, col) :
        def box_index(row, col): return (row // n) * n + col // n

        # Create all of our sets (which is how we track adding/removing for backtrack)
        rows = [set() for i in range(N)]
        cols = [set() for i in range(N)]
        boxs = [set() for i in range(N)]

        # Initialize the values with things that are already in grid
        for r in range(N):
            for c in range(N):
                if board[r][c] != '.':
                    value = int(board[r][c])
                    # place into the rows/cols/boxs set should be a func
                    addToSets(value, r, c)

        solved = False
        backtrack()


# Score Card
# Did I need hints? Y
# Did you finish within 30 min? Noooooo oh god
# Was the solution optimal? Oh yea however I needed lots of hints although the backtracking was actually not the hard part
# Were there any bugs? I initially messed up passing in the next row/col by not increasing row when overflowing
#  1 1 3 3 = 2
