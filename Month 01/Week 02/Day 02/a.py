#  Decode Ways: https://leetcode.com/problems/decode-ways/
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
        def dfs(index=0):
            # Base Case
            if index == len(s):
                return 1

            if s[index] == '0':
                return 0

            if index == len(s) - 1:
                return 1

            # I accidently added a bug my initial though for making this was with a for loop
            # however that basically makes this run indefinitely so I had to change it to a
            # recurse which I should of known in the first place
            count = dfs(index + 1)
            # Otherwise go down by two
            if int(s[index:index+2]) <= 26:
                count += dfs(index+2)

            return count

        return dfs()

    # Can we improve on this? Yes!
    # We can memoize!

    def numDecodingsMemo(self, s: str) -> int:
        def dfs(index=0):
            # Base Case
            if index == len(s):
                return 1

            if s[index] == '0':
                return 0

            if index == len(s) - 1:
                return 1

            # Since we are actually going down 1 at a time first and then by 2s
            # we are actually repeating work
            count = dfs(index + 1)
            # Otherwise go down by two
            if int(s[index:index+2]) <= 26:
                count += dfs(index+2)

            self.memo[index] = count
            return count

        self.memo = {}
        return dfs()

    # The dynamic programming solution is almost identical to above except you check how many you had before
    # instead of adding to the stacked value
    def numDecodingsDP(self, s: str) -> int:
        # The array has an extra spot because creating solutions that start with a len of 2
        dp = [0] * (len(s) + 1)
        # Create base case where if s[0] is not 0 we have at least one possible so far
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, len(dp)):

            # Check 1
            if s[i-1] != '0':
                dp[i] = dp[i-1]

            # Check 2
            temp = int(s[i-2: i])
            if 10 <= temp and temp <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]

# Score Card
# Did I need hints? Y
# Did you finish within 30 min? Y
# Was the solution optimal? Pretty well although there is a dynamic programming solution and there is even a o(n) with two pointers
# This actually kind of reminds of finding the fibonaci where it is based off the two previous answers
# Were there any bugs? My base cases need to be in a certain order and what I mentioned in the problem
#  3 3 1 3 = 2.5
