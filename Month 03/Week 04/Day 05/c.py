# Minimum Remove to Make Valid Parentheses: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

# In this problem we need to parse through the string and keep track of where valid parens are and remove them
# Anytime we have an invalid ) we can tell as there won't be  ( to catch it and so we can mark the index
# if there are valid we simply remove ( index and at the end we re parse the string and skip over
# any value in our stack

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)

            elif s[i] == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)

        toRemove = set(stack)
        result = ""

        for i in range(len(s)):
            if i not in toRemove:
                result += s[i]

        return result

# This works and runs in O(N) time and space


# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 8
# Was the solution optimal? Yup
# Were there any bugs? None
# 5 5 5 5 = 5
