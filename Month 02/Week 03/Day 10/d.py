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

# My solution to this problem is a recursive solution in which you move either one step down or by two if it is a number
# between 10->26

# We know that we are at a solution if are at the last index if we hit a zero we know that path cannot be the start of the next
# path

from os import curdir


class Solution:
    def numDecodings(self, s: str) -> int:
        self.memo = {}

        def dfs(index=0):
            # If we have the result already just return it
            if index in self.memo:
                return self.memo[index]

            # If we increased by two and ended up one over that is a valid solution
            if index == len(s):
                return 1

            if s[index] == '0':
                return 0

            # If we are at the last spot moving one or two is not possible
            # but we have a valid solution (so long as it isnt 0 which is caught above)
            if index == len(s) - 1:
                return 1

            count = dfs(index + 1)
            # Now we need to check going two at a time from current
            possible = int(s[index:index+2])
            if possible < 27:
                count += dfs(index+2)

            self.memo[index] = count
            return count

        return dfs()

# So the above works but can we do any better? It is a simple dp problem if we add memoization!
# I am going to do this in place because it is relatively easy

# Now the above runs in o(N) as we will step through the whole list and o(N) space to keep our memoization
# The question is can we do better than this? if you look at the way this problem is setup you realize
# That our solution comes from what is at 2 back and 1 back so if we keep updating these numbers we should
# find the optimal solution and our cache becomes two vars aka o(1) space

    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        # In our first case we want the two back to be set to one as it is possible but we
        # will start our index from 1
        twoBack, oneBack = 1, 1

        for i in range(1, len(s)):
            # get a var for adding oneBack and twoBack to be our new oneBack
            combo = 0

            # if s[0] != 0 one back has to stay what it is as 1 isn't possible
            if s[i] != '0':
                combo = oneBack

            # Now create the two digit and see if it is with 10 -> 26
            possible = int(s[i-1:i+1])
            if 9 < possible and possible < 27:
                # So if a variable between 10->26 exist we need to add all possible previous combos with
                # twoBack
                combo += twoBack

            twoBack = oneBack
            oneBack = combo

        # At the very end our last result will be in oneBack
        return oneBack

# Oh yeah this works and is optimized.

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 30
# Was the solution optimal? This is optimal
# Were there any bugs? No
# 5 5 5 5 = 5
