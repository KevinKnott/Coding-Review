# Valid Parentheses: https://leetcode.com/problems/valid-parentheses/
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# Stack problem super simple move through array adding to q unless the char is an ending bracket
# pop off if you hit matching bracket you are good else if you hit anything else false
from collections import deque


class Solution:
    def isValid(self, s):
        stack = deque()
        match = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in '(,[,{':
                stack.append(char)
            else:
                if len(stack) == 0 or stack.pop() != match[char]:
                    return False

        # I forgot that I need to check if the array is empty because I append just ( and it could be left on
        return len(stack) == 0


# Score Card
# Did I need hints? N
# Did you finish within 30 min? Y
# Was the solution optimal? Oh yea
# Were there any bugs? The bug I mentioned above
#  5 5 5 3 = 4.5
