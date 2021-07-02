# Count Binary Substrings: https://leetcode.com/problems/count-binary-substrings/

# Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
# Substrings that occur multiple times are counted the number of times they occur.

# We can move across the array and keep track off the number of values before that are the same and every time we switch check how many were before and take that as our count

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prevCount, result, curCount = 0, 0, 1

        for index in range(1, len(s)):
            if s[index-1] != s[index]:
                result += min(curCount, prevCount)
                prevCount, curCount = curCount, 1
            else:
                curCount += 1

        return result + min(curCount, prevCount)

# The above actually works really well and is actually the most optimal as it runs in o(n) and o(1). My initial thought was exactly on.
# This problem was actually a lot easier when I thought of it as a dynamic programming problem even though it really is more of a
# slidding window problem where you reset your count by alternating the counts


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 13 min
# Was the solution optimal? See the above
# Were there any bugs? I accidently started my curcount at 0 when it should have been at 1 because we always
# start where it switches
# 5 5 5 3 = 4.5
