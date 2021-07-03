# Basic Calculator II: https://leetcode.com/problems/basic-calculator-ii/

# Given a string s which represents an expression, evaluate this expression and return its value.
# The integer division should truncate toward zero.
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().


# So this problem wants us to figure out expressions and honestly we have to worry about having the correct order of operations
# Luckily we know that we can do any */ first and then any +- after so we could loop through the string twice doing the first
# two and then the second two

# Or we can use a stack and evaluate all */ as we go and then pop off the stack to evaluate the +- also this
# is made even easier since we don't have negtives

class Solution:
    def calculate(self, s: str) -> int:
        stack = []

        # This is to get the editor to stop complaining
        operand = 0
        sign = '+'
        for index in range(len(s)):
            if s[index].isdigit():
                operand = (operand * 10) + int(s[index])

                # My initial thought had me doing the above in a while loop
                # just to speed things up but because of the white chars
                # this is a simpler solution

                # while index < len(s) and s[index].isdigit():
                #     operand = (operand * 10) + int(s[index])
                #     index += 1

            if s[index] in '+-/*' or index == len(s) - 1:
                if sign == "+":
                    stack.append(operand)
                elif sign == "-":
                    stack.append(-operand)
                elif sign == "*":
                    stack.append(stack.pop()*operand)
                else:
                    stack.append(int(stack.pop()/operand))

                # Reset the values for next number
                operand = 0
                sign = s[index]

        # Loop through and add everything because we have already done / * and made sure our numbers are negative if needed
        result = 0
        while len(stack) != 0:
            result += stack.pop()

        return result


# Score Card
# Did I need hints? Nope
# Did you finish within 30 min? 45
# Was the solution optimal? This is not the optimal solution you can use no stack in the above if you keep
# a running result variable and a operand variable
# Were there any bugs? Yes I had a slight hiccup with making sure we have negatives where they need to be
# 5 3 3 3 = 3.5
