# Count Binary Substrings: https://leetcode.com/problems/count-binary-substrings/

# Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
# Substrings that occur multiple times are counted the number of times they occur.

# This problem reminds me of a dynamic problem of having the fibonacci sequence almost. All we have to do is keep count of the number
# of the prevVal Count and when it swaps we update our cur count to prev and reset cur. With this all we have to do is count
# the min of the cur val and prev val to our result and wallah

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, cur = 0, 1
        result = 0

        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                result += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        return result + min(prev, cur)


# Honestly I have done this problem enough to know the math trick behind it but basically you keep track of each count and you can
# create all valid combos 1 1 0 0 and 1 0  so since the prev and cur count is two you know your result has 2 valid values

# This runs in O(n) and uses O(1) space

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 6
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
