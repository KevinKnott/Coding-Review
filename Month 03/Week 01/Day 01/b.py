# Basic Calculator II: https://leetcode.com/problems/basic-calculator-ii/

# Given a string s which represents an expression, evaluate this expression and return its value.
# The integer division should truncate toward zero.
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# So my first thought here is that we can use a stack to solve this problem because at the end of the day addition and subtraction
# are the same so we just need to evaluate * / as we go and then we can evalue everything left on the stack with addition
# we will have to be carefull about division as we are truncating towards zero

class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 0:
            return 0

        stack = []
        operand = 0
        sign = '+'

        for i in range(len(s)):
            char = s[i]
            if char is not ' ':
                # So we check if we have a number
                if char.isdigit():
                    operand = (10 * operand) + int(char)

            # Check if char is a operation or that this is the last value we see in case we have a multiplication
            # or division at the end and we need the last digit
            if char in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(operand)
                elif sign == '-':
                    stack.append(-operand)
                elif sign == '*':
                    stack.append(stack.pop()*operand)
                else:
                    stack.append(int(stack.pop()/operand))

                # Reset the values
                operand = 0
                sign = char

        result = 0
        while stack:
            result += stack.pop()

        return result

# So the above works really well! It runs in O(N) time and space but can we do better?
# I think the answer is yes because we will always know that we can add any value
# that is before the last operand ie 10 + 10 * 5 will not be affected by the first 10
# Unfortunately I am on a bit of a time crunch so I won't code this out today


# Score Card
# Did I need hints? Yes for the optimal solution
# Did you finish within 30 min? Yes but not with optimal
# Was the solution optimal? See above
# Were there any bugs?  I didn't really have any bugs
# 3 4 3 5 = 3.75
