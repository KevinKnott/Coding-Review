# Regular Expression Matching: https://leetcode.com/problems/regular-expression-matching/

# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# This problem is quite challenging actually it turns out to be a backtracking dfs where
# we try to move down the pattern and string until we reach the end. To do this we follow
# a few simple things we know if the first char is matching the pattern we can have
# a star meaning 0+ in the string or we can have just a match. If we don't match
# all we have to check for is . or return false

# The reason this is backtracking or dynamic programming is because if we take the *
# 0 or many we will most definitely know whether or not there is a match at a certain
# point from a subset of the problem so if we keep track of this with memoization
# we can slightly improve upon our solution

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        lenS, lenP = len(s), len(p)

        def matching(sIndex=0, pIndex=0):
            potential = (sIndex, pIndex)
            if potential in memo:
                return memo[potential]

            if pIndex == lenP:
                return sIndex == lenS

            firstMatch = sIndex < lenS and (
                s[sIndex] == p[pIndex] or p[pIndex] == '.')

            # So we have the two options I mentioned b4 either taking a matching char with either 0 or many
            if pIndex + 1 < lenP and p[pIndex + 1] == '*':
                # Either take 0 or many for 0 it means we have no match at the start
                memo[potential] = (matching(sIndex, pIndex + 2)
                                   or (firstMatch and matching(sIndex + 1, pIndex)))
            else:
                memo[potential] = firstMatch and matching(
                    sIndex + 1, pIndex + 1)

            return memo[potential]

        return matching()

# This problem is actually kind of tricky for me but it becomes simpler when take the few possibilities and slowly work
# them out on paper. This uses o(M*N) time and space as for every possible * we will have to iterate over potentially the
# whole work and since we are storing all pairs of sIndex and mIndex we use o(N) space in our dictionary

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 17
# Was the solution optimal? Yup
# Were there any bugs? None
# 5 5 5 5 = 5
