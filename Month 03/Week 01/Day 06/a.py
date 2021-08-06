# Basic Calculator: https://leetcode.com/problems/basic-calculator/

# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# So for this problem we will need to iterate over the string and we can simply do the math as we go this will work by
# getting the operands and simply doing the math unless we see a (. At this point we can simply push whatever we have
# onto a stack and continue evaluating until we hit a ). For basic eval you eval any time you see anything that isn't
# a number

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        operand, sign = 0, 1
        # 1 for positive -1 for negative

        for ch in s:
            if ch != ' ':
                if ch.isdigit():
                    operand = (operand * 10) + int(ch)
                else:
                    if ch == '+':
                        result += sign * operand
                        operand, sign = 0, 1
                    elif ch == '-':
                        result += sign * operand
                        operand, sign = 0, -1
                    elif ch == '(':
                        stack.append(result)
                        stack.append(sign)
                        result, sign = 0, 1
                    else:
                        result += sign * operand
                        result *= stack.pop()
                        result += stack.pop()
                        operand = 0

        # At the end here we need to put the last number on

        return result + (operand * sign)

# Dang son this is working out just like a peach! It runs in O(N) time and space as it will put a lot in
# a stack if there are lots of parenthesis

# Score Card
# Did I need hints? N
# Did you finish within 30 min? 20
# Was the solution optimal? Yuh
# Were there any bugs? Negative
# 5 5 5 5 = 5
