# Basic Calculator: https://leetcode.com/problems/basic-calculator/

# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# In this problem everything is simple enough and there are two approaches but both are stack based you can use recursion when you
# see a paren and evaluate everything within as we only have + and - and then return the result and evaluate as you go. Alternatively
# You could do a stack based solution in which you iteratively do the same and then use a stack to keep on the value and the sign (+/-)

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        result = 0
        operand = 0

        for char in s:

            if char.isdigit():
                operand = (operand * 10) + int(char)

            elif char == '+':
                result += sign * operand
                operand = 0
                sign = 1

            elif char == '-':
                result += sign * operand
                operand = 0
                sign = -1

            elif char == '(':
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1

            elif char == ')':
                result += sign * operand
                result *= stack.pop()
                result += stack.pop()

                operand = 0

        return result + (sign * operand)

# This works and is pretty simple it runs in O(N) and can use up to O(N) space as well

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 10
# Was the solution optimal? Oh yeah
# Were there any bugs? None
# 5 5 5 5 = 5
