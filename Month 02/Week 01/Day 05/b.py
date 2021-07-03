# Longest Palindromic Substring: https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the longest palindromic substring in s.

# This problem is quite interesting basically we need to do an o(n^2) check from a starting point can expand and stay a palindrome
# the interesting piece is that we have two types of starts one with single letters and one with 2 letters

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left, right

        resultLeft, resultRight = 0, 0

        # Set the start point as 1 and see length of how far we can expand
        for i in range(len(s)):
            left, right = expand(i, i)

            if resultRight - resultLeft < right - (left + 1):
                resultLeft, resultRight = (left + 1), right

        # Set the start point as 2 and see length of how far we can expand
        for i in range(1, len(s)):
            left, right = expand(i-1, i)

            if resultRight - resultLeft < right - (left + 1):
                resultLeft, resultRight = (left + 1), right

        return s[resultLeft:resultRight]

# Yoooo I absolutely crushed this problem out of the park my intuition was correct and it only took me 15 min to code this
# That being said using a function builtin takes up a bit more space but is definitely a cleaner looking solution

# This runs in o(n^2) time as we expand as far as we can from the starting point so this could potentially visit every
# node twice as far as space this uses O(1) although we use some stack space it is never more than 1 expansion


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 15 min
# Was the solution optimal? See above
# Were there any bugs? No bugs for me
# 5 5 5 5 = 5
