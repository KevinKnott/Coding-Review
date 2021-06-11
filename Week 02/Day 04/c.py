# Longest Palindromic Substring: https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the longest palindromic substring in s.

# My initial thought here is to create a sliding window to solve if a sub string from l -> r is a palindrome
# Although I think we will have to do the check for odd sized and even sized as we have two possible start conditions
# It could also be a dfs but I think that may be worse complexity


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        maxLength = 0

        for left in range(len(s)):
            right = left

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if right - left - 1 > maxLength:
                maxLength = right - left - 1
                result = (left + 1, right)

        for left in range(len(s)):
            right = left + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if right - left - 1 > maxLength:
                maxLength = right - left - 1
                result = (left + 1, right)

        return s[result[0]:(result[1])]

    # While the above works I didn't realize that my left, right would need updating based off of where the index is currently instead of left /right

    # So after reviewing the solution I think  that it would be best to convert the code I have above into using two separate methods
    def longestPalindrome2(self, s: str) -> str:
        if len(s) <= 1:
            return s

        left, right = 0, 0
        for index in range(len(s)):
            oneChar = self.expandOutward(s, index, index)
            twoChar = self.expandOutward(s, index, index + 1)
            maxLength = max(oneChar, twoChar)

            if maxLength > right - left:
                left = index - (maxLength - 1) // 2
                right = index + maxLength // 2

        return s[left: right+1]

    def expandOutward(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1

# Score Card
# Did I need hints? Y for index math on getting the split point
# Did you finish within 30 min? Y
# Was the solution optimal? My initial solution is optimal however I needed to a bit of extra refactoring for using another metho
# Were there any bugs? I initially was off by one on length because of hitting -1  and not changing length with a minus 1
#  4 4 3 2 = 3.25
