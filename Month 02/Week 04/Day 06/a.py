# Regular Expression Matching: https://leetcode.com/problems/regular-expression-matching/

# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

#     '.' Matches any single character.​​​​
#     '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).


# Okay for this problem we simply create a backtracking dfs problem with caching. This is because for an string s and pattern p
# we can try moving down one by one for a matching char or check if the pattern allows for a . or a * and their rules
# the backtracking is needed as we have a star and that means it could be 0 or many of the same proceeding character aaa == aaa* or a*

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        sLength, pLength = len(s), len(p)

        def dfs(sIndex=0, pIndex=0):
            key = (sIndex, pIndex)
            if key not in cache:
                # If we are at end of the pattern we should check to see if we
                # are at the end of sIndex if so we return True
                if pIndex == pLength:
                    return sIndex == sLength

                # Check if we have a (x)* or a .
                # To do this we have to check if the first char matches
                firstMatch = sIndex < sLength and (
                    s[sIndex] == p[pIndex] or p[pIndex] == '.')

                # Check if we can use a *
                if pIndex + 1 < pLength and p[pIndex + 1] == "*":
                    # Use 0 possible (char)* or (the first match and x possible solutions meaning our pattern doesn't move)
                    cache[key] = dfs(sIndex, pIndex +
                                     2) or (firstMatch and dfs(sIndex + 1, pIndex))
                    # if not a missing character is invalid
                # If we aren't using a star we have to have a first match and move s and p
                else:
                    cache[key] = firstMatch and dfs(sIndex + 1, pIndex + 1)

            return cache[key]

        return dfs()

# So my first solution above didn't have a memoization but since we are backtracking in this case we know it is possible to reach a state we
# have already checked so if we simply store this in the cache and any time we hit that point we return the answer we should get a more optimal solution
# because without memo this would be something horendous like o((S+P) * 2 ^ (S+P)) and O(S^2 p^2) space

# With the memoization this is reduced to O(SP) for time and space as we simply run through once and if we hit a solution we have the answer for we
# return it instead of recomputing it

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 25
# Was the solution optimal? See blurb
# Were there any bugs? No bugs
# 5 5 5 5 = 5
