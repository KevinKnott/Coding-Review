# Minimum Window Substring: https://leetcode.com/problems/minimum-window-substring/

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique. A substring is a contiguous sequence of characters within the string.

# In this problem we have a sliding window except that we need to keep an extra count of how many actuall counted letters we need as we can have duplicates
# other than that it is very standard. We will expand our window until we have a solution then we will remove as many as possible from the solution until
# we no longer have a valid string than we will see if that is the shortest string we have found.

from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = None
        left = 0

        ourCount = Counter(t)
        totalNeeded = sum(ourCount.values())

        for right in range(len(s)):
            if s[right] in ourCount:
                if ourCount[s[right]] >= 1:
                    totalNeeded -= 1
                ourCount[s[right]] -= 1

            if totalNeeded == 0:
                while left < right and totalNeeded == 0:
                    if s[left] in ourCount:
                        ourCount[s[left]] += 1
                        if ourCount[s[left]] >= 1:
                            totalNeeded += 1
                            break
                    left += 1

                if result is None or result[1] - result[0] > right + 1 - left:
                    result = [left, right + 1]

                left += 1

        return '' if result is None else s[result[0]:result[1]]

# Alright alright alright
# Pretty much everything is in the first paragraph but this will run in O(N) and use o(M) space where M is the lenght of the target string

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 10
# Was the solution optimal? Yup
# Were there any bugs? None
# 5 5 5 5 = 5
