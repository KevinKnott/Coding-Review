#  Decode Ways: https://leetcode.com/problems/decode-ways/
# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.
# In order to decode the string we have two options
# Decode just one piece or decode two pieces if we see a 0 at a new start it is invalid
# Also we can simply hash this to improve performance


class Solution:
    def numDecodings(self, s):
        self.memo = {}

        def dfsDP(s, index=0):
            if len(s) == index:
                return 1
            if index in self.memo:
                return self.memo[index]
            # if index + 1 :
            #     return 1

            if s[index] == '0':
                return 0

            if len(s) - 1 == index:
                return 1

            count = dfsDP(s, index+1)
            if int(s[index:index+2]) <= 26:
                count += dfsDP(s, index + 2)

            self.memo[index] = count

            return self.memo[index]
        return dfsDP(s)

# Can we improve upon this solution?
# I think it is possible so we are checking the value at every spot
# But as we move across the value it should be possible to actually
# track the values

#

    def numDecodingsIterative(self, s):
        dp = [0] * (len(s)+1)

        dp[0] = 1  # for going two back

        dp[1] = 1 if s[0] != '0' else 0

        # we need to go forward from one to end and if it doesn't equal 0 continue
        for i in range(2, len(dp)):
            if s[i-1] != '0':
                dp[i] = dp[i-1]

            temp = int(s[i-2:i])
            if 10 <= temp and temp <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]


#  Is there an even better improvment?
#  I think that there may be as we have only two numbers ever being accesed
#  so if we could take the number and then update it as we go we could reduce the space complexity

# Score Card
# Did I need hints? Yes, i actually messed up the initial dp setup
# Did you finish within 30 min? y
# Was the solution optimal? Somewhat technically I think we could imrpove the space complexity
# Were there any bugs? N
#  3 5 3 5 = 4
