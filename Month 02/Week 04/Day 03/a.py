# Count Binary Substrings: https://leetcode.com/problems/count-binary-substrings/

# Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
# Substrings that occur multiple times are counted the number of times they occur.

# This problem is super simple all we have to do is keep count of the number of x and number of y and then we will have the same
# number added to the count

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prevCount, curCount = 0, 1
        result = 0

        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                result += min(prevCount, curCount)
                prevCount, curCount = curCount, 1
            else:
                curCount += 1

        return result + min(curCount, prevCount)

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 5
# Was the solution optimal? This is optimal it runs in O(N) and uses o(1) space as we only have 3 vars
# Were there any bugs? Nope
# 5 5 5 5 = 5
