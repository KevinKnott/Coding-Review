# Decode Ways: https://leetcode.com/problems/decode-ways/

# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"

# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

#     "AAJF" with the grouping (1 1 10 6)
#     "KJF" with the grouping (11 10 6)

# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.

# The answer is guaranteed to fit in a 32-bit integer.

# In this problem it looks like we have a dynamic programming problem as we can make intelligent choices to move us forward
# and help us decode. Basically we will create a dfs that uses memoization as we can try moving as a one letter combo
# or a two letter combo from 1 -> 26 once we get towards the bottom we will see this makes a tree like the fib problem
# that is solvable with memoization

from os import curdir


class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def numWays(index=0):
            if index in memo:
                return memo[index]

            if index == len(s):
                return 1

            if s[index] == '0':
                return 0

            if index == len(s) - 1:
                return 1

            # Try 1
            count = numWays(index+1)

            # Try 2
            if index + 1 < len(s) and int(s[index:index+2]) <= 26:
                count += numWays(index + 2)

            memo[index] = count
            return memo[index]

        return numWays()

# So the above works like I mentioned it runs in O(N) time and space and is just like a memoization of fib and also
# num jumps

    def numDecodings(self, s: str) -> int:
        # Cant start at 0
        if s[0] == '0':
            return 0

        # Number of solution two back an done back
        oneBack, twoBack = 1, 1

        for i in range(1, len(s)):
            count = 0

            # All numbers are valid except 0
            # so take the number of solutions from before
            # and add them to count
            if s[i] != '0':
                count = oneBack

            # Now do the same for 2 but the values have to be between 10->26
            possibleSolution = int(s[i-1:i+1])
            if possibleSolution >= 10 and possibleSolution <= 26:
                count += twoBack

            twoBack = oneBack
            oneBack = count

        return oneBack

# This runs in O(N) time and uses O(1) space

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? Optimal except for space as we can convert this to an iterative approach like the fib problem using 2 vars
# Were there any bugs? No
# 5 5 5 5 = 5
