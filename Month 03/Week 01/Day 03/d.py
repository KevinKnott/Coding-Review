# Sudoku Solver: https://leetcode.com/problems/sudoku-solver/

# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

#     Each of the digits 1-9 must occur exactly once in each row.
#     Each of the digits 1-9 must occur exactly once in each column.
#     Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

# The '.' character indicates empty cells.

# This boils down from a really hard problem into a simple backtracking dfs solution
# basically what we need to do is create a set for rows, cols and the grid boxes
# once we have all those sets we move across from 0,0 -> 8,8 and if there is an empty box
# try and fill it with a value that is not in any of the three sets


class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # For checking we need to check if value is not in r, c or sqr
        def canAddVal(value, r, c):
            return value not in row[r] and value not in col[c] and value not in sqr[sqrIndex(r, c)]

        # So for adding we need to add the number to the set
        # and then to the board
        def addToBoard(value, r, c):
            board[r][c] = str(value)
            row[r].add(value)
            col[c].add(value)
            sqr[sqrIndex(r, c)].add(value)

        # Remove is the same as above but the opposite
        def remFromBoard(value, r, c):
            board[r][c] = '.'
            row[r].remove(value)
            col[c].remove(value)
            sqr[sqrIndex(r, c)].remove(value)

        def nextLocation(r, c):
            # Check if we are at the final location because if we are we simply need to return
            if r == N - 1 and c == N - 1:
                self.isSolved = True
                return
            else:
                # If we are here we need to move across col unless we are at edge
                if c == N - 1:
                    backtrack(r+1)
                else:
                    backtrack(r, c + 1)

        def backtrack(r=0, c=0):
            # For this solution we need try adding a number recursing down until it fails
            # then removing the number if it gets back
            if board[r][c] != '.':
                # This r,c already has a number so we skip over it
                nextLocation(r, c)
            else:
                # Otherwise try all possible numbers
                for val in range(1, 10):
                    if canAddVal(val, r, c):
                        addToBoard(val, r, c)
                        nextLocation(r, c)

                        # If we get to the end we just need to return
                        if self.isSolved:
                            return

                        # Otherwise backtrack by removing the added num
                        remFromBoard(val, r, c)

        # Set up the basic stuff we now
        n = 3
        N = n * n

        # Create sets for row col and the sqr (aka grid box)
        row = [set() for _ in range(N)]
        col = [set() for _ in range(N)]
        sqr = [set() for _ in range(N)]

        # Create a lambda to convert the r,c pair into a index of sqr for our set
        def sqrIndex(r, c): return (r // n * n) + (c // n)

        # Create a way to trigger the end if we are at the last spot
        self.isSolved = False

        # Loop through the whole entire grid and add numbers to our sets
        for r in range(N):
            for c in range(N):
                if board[r][c] != '.':
                    addToBoard(int(board[r][c]), r, c)

        backtrack()

        return board

# The above works out and runs in a horrible O(9!) which reduces to o(1) and uses o(!) space as well

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 25
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
