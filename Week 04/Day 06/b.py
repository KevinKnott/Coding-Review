# Minimum Remove to Make Valid Parentheses: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

#     It is the empty string, contains only lowercase characters, or
#     It can be written as AB (A concatenated with B), where A and B are valid strings, or
#     It can be written as (A), where A is a valid string.

# My initial thought here is we could use backtracking to solve this problem however backtracking is normally quite expensive o(n^2)
# so my second thoguht is to use a stack and keep a balance going and remove the anything that makes the balance uneven

# I think this problem will have a hard time as when we are removing we need to track where the thing is we are removing

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        toRemove = set()

        for index, char in enumerate(s):
            if char == '(':
                stack.append(index)

            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    toRemove.add(index)

        while stack:
            toRemove.add(stack.pop())

        result = ''
        for index in range(len(s)):
            if index not in toRemove:
                result += s[index]

        return result

# My initial thought actually made this problem quite easy the onlly thing that I haven't considered is that instead of removing all
# elements immediately from the string we can build a list of indicies that we actually need to remove and remove them after
# This runs in o(n) time and space and is pretty striaght forward

# Can we do better? The above steps that I could do can be combined so that you are only adding valid results to the string
# however we will do it in two passes but at the same time it is the same complexity as above but more complicated code

    def minRemoveToMakeValidCombined(self, s: str) -> str:
        firstPass = []
        balance = 0
        open = 0

        # Remove all invalid ')'
        for c in s:
            if c == "(":
                balance += 1
                open += 1
            elif c == ")":
                # Ignore if there is a valid pair
                if balance == 0:
                    continue
                balance -= 1
            firstPass.append(c)

        # Remove the worst '('
        result = []
        # We want to remove the first ( that breaks the answer
        numValidOpen = open - balance

        for c in firstPass:
            if c == "(":
                numValidOpen -= 1
                if numValidOpen < 0:
                    continue
            result.append(c)

        return ''.join(result)

# Score Card
# Did I need hints? Yeah I took a peak to see if my balancing was the right idea but I coded it on my own
# Did you finish within 30 min? Y 25 min
# Was the solution optimal? Y the code runs in o(n) for time and space which seems to be optimal
# Were there any bugs?  I didn't run into any bugs
# 4 5 5 5 = 4.75
