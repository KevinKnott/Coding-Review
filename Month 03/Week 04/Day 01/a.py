# Basic Calculator II: https://leetcode.com/problems/basic-calculator-ii/

# Given a string s which represents an expression, evaluate this expression and return its value.
# The integer division should truncate toward zero.
# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# In this problem we have two options for what we can do: either we go throught he string and simple make all additions/subtractions
# happen at the end with a stack and solve for any * or / immediately. Alternatively you can use an extra variable to keep track
# of the last variable as any time you need to use * or / it will only go back one and if not you can simply calculate as you go
# through the string

class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 0:
            return 0

        stack = []
        operand = 0
        sign = '+'

        for i in range(len(s)):
            ch = s[i]

            if ch.isdigit():
                operand = (operand * 10) + int(ch)

            if ch in '+-/*' or i == len(s) - 1:
                if sign == '+':
                    stack.append(operand)
                elif sign == '-':
                    stack.append(-operand)
                elif sign == '*':
                    stack.append(stack.pop() * operand)
                else:
                    stack.append(int(stack.pop()/operand))

                operand = 0
                sign = ch

        result = 0

        while stack:
            result += stack.pop()

        return result

# So this works and is actually pretty optimal it runs in O(N) time and space but we can do better as I said.
# As you know I can just keep track of the last which would be equivalent to the stack.pop() above

    def calculate(self, s: str) -> int:
        if len(s) == 0:
            return 0

        result = 0
        last, cur = 0, 0
        sign = '+'

        for i in range(len(s)):
            ch = s[i]

            if ch.isdigit():
                cur = (cur * 10) + int(ch)

            if ch in '+-/*' or i == len(s) - 1:
                if sign == '+':
                    result += last
                    last = cur
                elif sign == '-':
                    result += last
                    last = -cur
                elif sign == '*':
                    last = last * cur
                else:
                    last = int(last / cur)

                cur = 0
                sign = ch

        result += last

        return result

# Aaaand boom a sexy transformation which saves us on space complexity.
# This will run in O(N) time and O(1) space as we are calculating on the fly

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 17
# Was the solution optimal? Oh yeah
# Were there any bugs? Nope
# 5 5 5 5 = 5
