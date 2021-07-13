# Minimum Window Substring: https://leetcode.com/problems/minimum-window-substring/

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# A substring is a contiguous sequence of characters within the string.

# haha this is obviously a sliding window problem as we have the word window
# Jokes aside we to create a count out of t and then if we reach total count of 0
# start reducing the substring until we no longer have a solution
# Each time keeping track of the best solution

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ourCount = Counter(t)
        totalLeft = sum(ourCount.values())
        result = None

        left = 0
        for right in range(len(s)):
            # add right char
            if s[right] in ourCount:
                if ourCount[s[right]] > 0:
                    totalLeft -= 1
                ourCount[s[right]] -= 1

            if totalLeft == 0:
                # check if we have totalLeft = 0 make sure left doesn't pass right
                while left < right and totalLeft == 0:
                    # remove left char
                    if s[left] in ourCount:
                        ourCount[s[left]] += 1

                        if ourCount[s[left]] > 0:
                            totalLeft += 1
                            break

                    left += 1

                # Check if we have an optimal solution
                # Remember that end + 1 is need because splicing in python is [x:y)
                if result is None or ((right + 1) - left) < (result[1] - result[0]):
                    result = [left, right+1]

                left += 1

        return "" if result is None else s[result[0]:result[1]]


# The above works and is quite a banging solution honestly. It runs in o(N+M) time and uses o(N+M)
# as in the worst case we will have both strings fully in the count as they match

# Can we improve this solution? We should be able to instead of trying to increment the left side
# of the pointer one by one we could theoretically just store the index of the next needed char
# that way you can skip right over to the next time you remove a needed char you would have to do this
# before you start the sliding window and it would take up a bit more space but would reduce the solution

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 30
# Was the solution optimal? See above
# Were there any bugs? I forgot that my splicing makes the result off by one if I am not careful
# 5 5 3 4 = 4.25
