# Minimum Window Substring: https://leetcode.com/problems/minimum-window-substring/

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# A substring is a contiguous sequence of characters within the string.

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Count what we have in some sort of bit array
        needed = Counter(t)
        remainingNeeded = sum(needed.values())

        left, right = None, None

        start = 0
        # Loop through all characters in s
        for end in range(len(s)):
            currentChar = s[end]
            if currentChar in needed:
                if needed[currentChar] > 0:
                    remainingNeeded -= 1
                needed[currentChar] -= 1

            if remainingNeeded == 0:

                # Pop off characters
                while start < end and remainingNeeded <= 0:
                    removeChar = s[start]
                    if removeChar in needed:
                        needed[removeChar] += 1
                        if needed[removeChar] > 0:
                            remainingNeeded += 1
                            break

                    start += 1

                # Check for if the current result is less then previous
                if left is None or (end + 1 - start) < (right - left):
                    left, right = start, end + 1

                start += 1

        # If nothing was found return ""
        return "" if left is None else s[left:right]

# Can this be improved upon? We can improve the speed of this problem if instead of traversing across i poping off every value we simply
# create a q of the next letter in t that we need  and skip to that letter and do the equivalent parsing as above

# This solution technically runs in O (S+T) where S and T is the lengths as we can parse through all of S and all of t and space is o(T) since we have to
# track all the values that we may need

# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Kind of there is one slight improvement that I think can be made
# Were there any bugs? Nope!
#  4 5 3 3 = 3.75
