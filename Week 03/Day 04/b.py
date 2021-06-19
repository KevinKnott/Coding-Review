# Minimum Window Substring: https://leetcode.com/problems/minimum-window-substring/

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# A substring is a contiguous sequence of characters within the string.

from collections import Counter


class Solution:
    def minWindow(self, s, t):
        seen = Counter(t)
        minResult = -1

        for i in range(len(s)):
            temp = Counter()

            if s[i] not in t:
                continue

            for j in range(i, len(s)):
                if s[j] in seen:
                    if seen[s[j]] != 0:
                        temp[s[j]] += 1
                        seen[s[j]] -= 1

                if all(seen[key] == 0 for key in seen.keys()):
                    if minResult == -1 or (j - i) < (minResult[1] - minResult[0]):
                        minResult = [i, j+1]
                    break

            for key, value in temp.items():
                seen[key] += value

        return "" if minResult == - 1 else s[minResult[0]:minResult[1]]

# Is this the most efficient way? Definitely not this is actually a horrible run time of o(n^2) and o(t) space
# The more optimal way to solve for this problem is to actaully start at an index and go to length t counting what is there
# Once you are at len(t) you check if you have all the values if not increase the window to the right until you have it
# then once you have all values check if it is shortest you decrease the left side until you have removed the desirable result
# Then you increase to the right again

    def minWindowBasic(self, s, t):
        seen, missing = Counter(t), len(t)
        minResult = None

        start = 0
        end = 0
        while end < len(s):
            if s[end] in seen:
                if seen[s[end]] > 0:
                    missing -= 1
                seen[s[end]] -= 1

            # If we have all values check if we have new result
            # and then increase start
            if not missing:
                # Try to see if we can remove duplicated letters
                while start <= end and not missing:
                    if s[start] in seen:
                        seen[s[start]] += 1
                        if seen[s[start]] > 0:
                            missing += 1
                            break
                    start += 1

                if minResult is None or end - start <= (minResult[1] - minResult[0]):
                    minResult = [start, end]

                start += 1

            end += 1

        # if minResult[1] == len(s) - 1:
        #     minResult[1] -= 1
        return "" if minResult is None else s[minResult[0]:(minResult[1]+1)]

# Score Card
# Did I need hints? Y
# Did you finish within 30 min? 2 hours
# Was the solution optimal? No idea
# Were there any bugs? I spent so long trying to figure out why I was off by one but it turns out I wasn't ending the loop until start < len(s)
#  3 1 1 1
