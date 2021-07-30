# Minimum Window Substring: https://leetcode.com/problems/minimum-window-substring/

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# A substring is a contiguous sequence of characters within the string.


# This problem seems really difficult but it turns out that it is simply a sliding window with one slight exception that we can have duplicate
# characters in our target string so we will move left to right until we have all required values
# then we will pop off until that is no longer the case and see if it is shorter than the overall result
# then we simply return that result

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = None
        needed = Counter(t)
        remaining = sum(needed.values())

        left = 0
        for right in range(len(s)):
            # Check if current char is in our needed values
            # and add it
            if s[right] in needed:
                if needed[s[right]] > 0:
                    remaining -= 1
                needed[s[right]] -= 1

            # check if remaining is 0
            if remaining == 0:
                # if so remove one letter at a time from the left until we no longer have an answer
                while left < right and remaining == 0:
                    if s[left] in needed:
                        needed[s[left]] += 1

                        if needed[s[left]] > 0:
                            remaining += 1
                            # break to make sure we can check result
                            break

                    left += 1

                # check if we have a new result
                if result is None or result[1] - result[0] > (right + 1) - left:
                    # remember to add 1 as python slice is [x: y)
                    result = [left, (right + 1)]

                # Remember to move left past the needed char
                left += 1

        return '' if result is None else s[result[0]: result[1]]

# The above works and runs in O(N) time and space where N is the length of s + length of T
# this is because we potentially have to parse through every letter of the string and of the target


# Score Card
# Did I need hints? N
# Did you finish within 30 min? 13
# Was the solution optimal? This is optimal
# Were there any bugs? No
# 5 5 5 5 = 5
