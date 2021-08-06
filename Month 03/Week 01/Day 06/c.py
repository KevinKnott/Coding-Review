# Longest Palindromic Substring: https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the longest palindromic substring in s.

# So for this problem we could manually check from starting from i to j if we have a possible longest palindrome
# and keep reducing the size until we hit 0 but this is quite computationally heavy
# So I think a better approach is to run through the s 2 times trying to expand out as far as possible from every
# i i and i i+1 combination until we get the right result

class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Create a sub function that does the expansion from a x,y pair and returns the indicies of the farthest out
        # it can expand
        def expand(x, y):

            while x >= 0 and y < len(s) and s[x] == s[y]:
                x -= 1
                y += 1

            return (x, y)

        longestPalindrome = [0, 0]

        # expand for abcba
        for i in range(len(s)):
            left, right = expand(i, i)

            if longestPalindrome[1] - longestPalindrome[0] < right - (left+1):
                longestPalindrome = [(left + 1), right]

        # Expand from xyyx
        for i in range(1, len(s)):
            left, right = expand(i-1, i)

            if longestPalindrome[1] - longestPalindrome[0] < right - (left+1):
                longestPalindrome = [(left + 1), right]

        return s[longestPalindrome[0]:longestPalindrome[1]]


# The above is pretty easy once you think about the solution. This runs in O(n^2) instead of o(n^3) and
# and it uses O(1) space

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 15
# Was the solution optimal? Oh yeah
# Were there any bugs? None
# 5 5 5 5 = 5
