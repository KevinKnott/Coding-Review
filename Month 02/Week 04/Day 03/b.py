# Minimum Remove to Make Valid Parentheses: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

# In this problem we can take a stack keep track of all indicies of parens and then keep a number of the overall balance
# if the balance is every - or there are some remaining after we simply add them to the removal list

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove = set()
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) > 0 and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    remove.add(i)

        while stack:
            remove.add(stack.pop())

        result = ''
        for i in range(len(s)):
            if i not in remove:
                result += s[i]

        return result

# The above works and runs in o(N) and uses o(N) space I believe this is optimal as we will alwaus
# need to parse every element at least onece

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? See above
# Were there any bugs?  I didn't really have any bugs
# 5 5 5 5 = 5
