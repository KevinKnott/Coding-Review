# Valid Parentheses: https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# This is actually another super easy problem all we have to do is keep adding all values onto the stack
# until we see a closing bracket then we check if the top of stack matches if it does continue else
# return false if the stack is not empty at the end it is also invalid

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        match = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in match:
                if len(stack) == 0 or stack[-1] != match[char]:
                    return False

                stack.pop()

            elif char in '([{':
                stack.append(char)

        return len(stack) == 0

# This runs in o(n) time and space and is optimal

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 7
# Was the solution optimal? This is optimal
# Were there any bugs? No
#  5 5 5 5 = 5
