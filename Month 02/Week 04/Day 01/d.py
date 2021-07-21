# Regular Expression Matching: https://leetcode.com/problems/regular-expression-matching/

# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

#     '.' Matches any single character.​​​​
#     '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# This looks like a simple recursion problem which we may be able to add in memoization for piece we have already computed
# For instance using a . is quite simple as you just move along the pattern but for * it is complicated because you either
# move x chars down or potentially 0. Which honestly sounds like backtracking

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        lengthS, lengthP = len(s), len(p)

        def backtrack(sIndex=0, pIndex=0):
            # Create a key and check if we can return result we have seen
            key = (sIndex, pIndex)
            if key not in memo:

                # Check if we have no more pattern to match because if s has values but p is empty we return false
                if pIndex == lengthP:
                    return sIndex == lengthS

                # Check first if we have two letters so we can move down or check if we have a . as that is any one char
                firstMatch = sIndex < lengthS and (
                    p[pIndex] == s[sIndex] or p[pIndex] == '.')

                # Check if the pattern as a posibility of *
                if pIndex < lengthP - 1 and p[pIndex+1] == '*':
                    # Here we check our two options where we have no * match and change pattern
                    # or we match first char and have 0 -> x times so we move down s
                    memo[key] = (
                        backtrack(sIndex, pIndex + 2)) or (firstMatch and backtrack(sIndex+1, pIndex))
                else:
                    # If we dont have a valid star we check if the first match and continue down
                    # this is the nomral possibility
                    memo[key] = firstMatch and backtrack(
                        sIndex+1, pIndex+1)

                # Afterwards we need to propogate back up the backtracking
                return memo[key]
            else:
                return memo[key]

        return backtrack()

# Score Card
# Did I need hints? Y
# Did you finish within 30 min? 30
# Was the solution optimal? This is optimal but I honestly don't know the complexity probably O(TP) for time and space where T and P are the len of strings
# Were there any bugs? No
# 2 2 3 4 = 2.75
