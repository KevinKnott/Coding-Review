# Regular Expression Matching: https://leetcode.com/problems/regular-expression-matching/

# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where:

#     '.' Matches any single character.​​​​
#     '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# Okay so this problem seems to me like we have a recursive decent algo where we go down
# a string and see if it matches the pattern the two caveats are that . can match anything once
# and * can match the prev char 0 or more times. So basically this becomes a backtracking problem


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.memo = {}

        def search(s, p):
            key = (s, p)
            if key not in self.memo:
                # Basically continue down unless we have finished our pattern
                if not p:
                    # Then our result will be if s is empty
                    return not s

                # Okay so we have two cases we have two letters in which case we just move down
                firstMatch = len(s) != 0 and (p[0] == s[0] or p[0] == '.')

                # Since first match covers our normal moves let us consider moving down with a star
                # So we check if p has two values char and *
                if len(p) >= 2 and p[1] == '*':
                    # If it does we need to check either having no match or matching continues
                    # The first half is in case we have a match of 0 length and we need to move past the pattern
                    # the second half is if we have a match to our * but we need to check if there are mutliple chars
                    self.memo[key] = (search(s, p[2:])) or (
                        firstMatch and search(s[1:], p))
                else:
                    # Here we just continue down as normal
                    self.memo[key] = firstMatch and search(s[1:], p[1:])

                return self.memo[key]
            else:
                return self.memo[(s, p)]

        return search(s, p)

# okay so my initial thought on backtracking isn't quite right it is simpley a divide and conquer dp problem
# luckily I have seen this problem before and knew that the recursive solution is close to correct I did forget for a bit that
# we actually needed to not return immediately if the values don't match as we may have a case where the pattern has a star
# This solution will run in o(SP) as we have S and P and we will need to in worse case go down both all the way
# The space complexity could be o(1) if I didn't add memoization to this problem. With the memoization the problem is also
# o(SP)


# Score Card
# Did I need hints? Y
# Did you finish within 30 min? 25
# Was the solution optimal? This is optimal
# Were there any bugs? No
# 1 4 5 5 = 3.75
