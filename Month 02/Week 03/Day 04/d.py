# Sudoku Solver :https://leetcode.com/problems/sudoku-solver/

# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

#     Each of the digits 1-9 must occur exactly once in each row.
#     Each of the digits 1-9 must occur exactly once in each column.
#     Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

# The '.' character indicates empty cells.

# So this problem seems rather complicated. However when we apply a backtracking dfs solution
# this problem becomes easier to write. Basically we will continue trying every possible remaining option
# From the set of values 1-9 left after considering following sets: Row, Col and Square if we run out of options
# remove the last value and continue trying until we have reached the last square

class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # For any backtracking problem we need a few steps
        # Check if you can place an element as they can't be in any set
        def canAddVal(value, r, c):
            return value not in row[r] and value not in col[c] and value not in sqr[sqrIndex(r, c)]

        # Add an element
        def addToBoard(value, r, c):
            row[r].add(value)
            col[c].add(value)
            sqr[sqrIndex(r, c)].add(value)
            board[r][c] = str(value)

        # Remove an element
        def remFromBoard(value, r, c):
            row[r].remove(value)
            col[c].remove(value)
            sqr[sqrIndex(r, c)].remove(value)
            board[r][c] = '.'

        # Move forward
        def nextLocation(r, c):

            if r == N-1 and c == N-1:
                self.isSolved = True
                return
            else:
                if c == N - 1:
                    backtrack(r + 1)
                else:
                    backtrack(r, c + 1)

        def backtrack(r=0, c=0):

            if board[r][c] != '.':
                # If the number already exists keep moving
                nextLocation(r, c)
            else:
                # iterate over all values 1-9 and try adding them
                for val in range(1, 10):
                    if canAddVal(val, r, c):
                        addToBoard(val, r, c)
                        nextLocation(r, c)

                        # Now that we have added if we end up solving
                        # we need return the result
                        if self.isSolved:
                            return

                        remFromBoard(val, r, c)

        # Set up box lengths
        n = 3
        N = n * n

        # There are 9 rows 9 col and 9 squares which influence which
        # nums can be chosen
        row = [set() for _ in range(N)]
        col = [set() for _ in range(N)]
        sqr = [set() for _ in range(N)]

        # This formula comes from the fact squares in sudoku work like this:
        # 0 1 2
        # 3 4 5
        # 6 7 8
        def sqrIndex(r, c): return (r // 3 * 3) + (c // 3)

        self.isSolved = False

        for i in range(N):
            for j in range(N):
                # Add all existing numbers to our sets
                if board[i][j] != '.':
                    addToBoard(int(board[i][j]), i, j)

        backtrack()

        return board


# So the above works the problem is for backtracking the time complexity is o(1) However
# in the worst case you have to run 9! possible combinations minus whatever combinations
# are removed from numbers already on the board.

# As for the space complexity it is also o(1) as we have 3 sets of 9 and then the 9 by 9 board


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 30
# Was the solution optimal? This is optimal
# Were there any bugs? No
# 5 4 5 5 = 4.75
