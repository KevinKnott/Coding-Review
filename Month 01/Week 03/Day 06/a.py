# Sudoku Solver: https://leetcode.com/problems/sudoku-solver/

# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

#     Each of the digits 1-9 must occur exactly once in each row.
#     Each of the digits 1-9 must occur exactly once in each column.
#     Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

# The '.' character indicates empty cells.

# This seems to me like a simple backtracking problem you track all elements in a 3 sets so you know what is allowed in each column row or box (3x3)
# then you add a value from 1-9 and continue processing until you reach the end. If you find a spot where you can't continue go back and change the value
# where you first started trying something new


class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def canPlaceValue(row, col, value):
            return not(value in inRow[row] or value in inCol[col] or value in inBox[box(row, col)])

        # Add a value to position
        def addValue(row, col, value):
            inRow[row].add(value)
            inCol[col].add(value)
            inBox[box(row, col)].add(value)
            board[row][col] = str(value)

        # Remove Value from position
        def removeValue(row, col, value):
            inRow[row].remove(value)
            inCol[col].remove(value)
            inBox[box(row, col)].remove(value)
            board[row][col] = '.'

        # Get next location
        def nextPosition(row, col):
            if row == N - 1 and col == N - 1:
                self.isSolved = True
                return
            else:
                if col == N - 1:
                    backtrackDFS(row + 1, 0)
                else:
                    backtrackDFS(row, col + 1)

        # Backtrack DFS

        def backtrackDFS(row, col):
            if self.isSolved:
                return

            # if row, col == '.' just get next position
            if board[row][col] != '.':
                nextPosition(row, col)
            else:
                # loop through 1-9
                for i in range(1, 10):
                    # Check if you can add value
                    if canPlaceValue(row, col, i):
                        addValue(row, col, i)
                        # If we have solved everything return
                        nextPosition(row, col)

                        if self.isSolved:
                            return

                        removeValue(row, col, i)

        n = 3
        N = n * n
        def box(row, col): return (row // n) * n + (col // n)
        self.isSolved = False

        # Create a set for each row col and box to statisfy the rules of sudoku
        inRow = [set() for _ in range(9)]
        inCol = [set() for _ in range(9)]
        inBox = [set() for _ in range(9)]

        # Add all values that are permanent into the above sets
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    addValue(row, col, int(board[row][col]))

        backtrackDFS(0, 0)
        return board


# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? yes
# Was the solution optimal? I wrote the optimal solution
# Were there any bugs? I forgot that I needed to have a short ciruit once I have solved the problem completely
#  5 5 5 3 = 4.5
