# https://leetcode.com/contest/weekly-contest-244/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/
# You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

# Type-1: Remove the character at the start of the string s and append it to the end of the string.
# Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
# Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

# The string is called alternating if no two adjacent characters are equal.

# For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

#  Initial thought this is a dynamic programming problem

# Only doing the optimal solutions because I couldn't solve
class Solution:
    def minFlips(self, s):
        n = len(s)
        s += s
        s1, s2 = '', ''

        # Create simple double string to solve for putting the beginning to the end

        for i in range(n):
            s1 += '0' if i % 2 == 0 else '1'
            s2 += '1' if i % 2 == 0 else '0'

        # track the number of differences between trying to create 10 to end and 01 to end

        ans1, ans2, ans = 0, 0, float('inf')
        for i in range(n):
            # print(ans1, ans2, ans)

            # If the string doesn't match the solution strings add 1 for flipping
            if s1[i] != s[i]:
                ans1 += 1
            if s2[i] != s[i]:
                ans2 += 1

            #  for each i over we have swapped front to back
            if i >= n:
                #  if our array is larger then our n we need to remove whatever was done on the other side if they didn't match
                if s1[i-n] != s[i-n]:
                    ans1 -= 1
                if s2[i-n] != s[i-n]:
                    ans2 -= 1

            # If we have a new potential solution check to find the smallest change in the current window
            if i >= n - 1:
                ans = min(ans1, ans2, ans)

        return ans
