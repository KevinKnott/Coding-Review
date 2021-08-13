# Valid Parentheses: https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.

# In this problem we can really boil this down to using a stack to check out whether the last bracket is the appropriate bracket
# and from there if we get the wrong one it is invalid or if the length of the stack is > 0 we know it is invalid

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenPair = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in '[({':
                stack.append(char)
            elif char in parenPair:
                if len(stack) == 0 or stack[-1] != parenPair[char]:
                    return False
                stack.pop()

        return len(stack) == 0

# This works and runs in O(N) time and uses O(N) space.

# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 4 minutes
# Was the solution optimal? O(N)
# Were there any bugs? None
# 5 5 5 5 = 5
