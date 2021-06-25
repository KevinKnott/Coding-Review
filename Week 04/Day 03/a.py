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

class Solution:
    def numDecodings(self, s: str) -> int:
        self.memo = {}

        def dfs(index=0):
            if index in self.memo:
                return self.memo[index]

            if index == len(s):
                return 1

            if s[index] == '0':
                return 0

            if index == len(s) - 1:
                return 1

            # Go one
            count = dfs(index+1)

            # Go two
            if int(s[index:index+2]) <= 26:
                count += dfs(index+2)

            # cache
            self.memo[index] = count
            return count

        return dfs()

# The above works and cuts out a lot of the problems that we have however this still runs in o(N) and o(N)
# Can we improve on this solution? I think so this is almost like the fibonaci sequence where we can keep track of the last
# two answers and create the new one thus moving up and using only o(1) space

    def numDecodingsImproved(self, s):
        if s[0] == '0':
            return 0

        # If the first number isn't 0 then we have a valid case
        # where two back is 1 but we skip over it by starting range at 1

        oneBack = 1
        twoBack = 1

        for i in range(1, len(s)):
            # Get a temp variable for combining the two results
            current = 0

            # make sure we don't have 0 because that makes going back two 0
            # Also oneBack should be 1 if it isnt 0 as 0 is the only invalid digit
            if s[i] == '0':
                current = oneBack

            twoDigit = int(s[i-1: i+1])
            # Make sure that our new two digit is between 10-26 (we don't want 35)
            if twoDigit >= 10 and twoDigit <= 26:
                current += twoBack

            # update the twoback and oneback to new values
            twoBack = oneBack
            oneBack = current

        return oneBack

# So the above should work but it does so because it is like the fib sequence we only need two vals to create thrid 1 1 = 1 2
# so you keep the value that you need and discard outside of the range like a window


# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y 25
# Was the solution optimal? I was able to create the optimal solution although I kind of skipped over the bottom up and tabulation that helps with
# creating the optimal solution as I have seen it before with the fib sequence
# Were there any bugs? I accidently pointed the second algo to current (because it is correct) but really I need to return oneBack because
# python can possibly clean up that val after the loop
# 5 5 5 3 = 4.5
